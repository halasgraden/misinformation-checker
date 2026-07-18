from fastapi import FastAPI, HTTPException
from factcheck import get_all_fact_checks
from claim import get_claims
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Review(BaseModel):
    rating: str | None = None
    url: str | None = None
    publisher: str | None = None

class ClaimItem(BaseModel):
    claim: str
    status: str
    reviews: list[Review] = []

class AnalysisResponse(BaseModel):
    url: str
    claims: list[ClaimItem]

class AnalysisRequest(BaseModel):
    url: str


def build_response(url, claims_with_results):
    output_claims = []

    for entry in claims_with_results:

        result = entry["result"]
        claim_text = entry["claim"] #pull data

        if "claims" in entry["result"] and len(entry["result"]["claims"]) > 0: #check if claim exists
            reviews = []
            for matches in result["claims"]:
                for review in matches.get("claimReview", []):
                    reviews.append({
                        "rating": review.get("textualRating"),
                        "url": review.get("url"),
                        "publisher": review.get("publisher", {}).get("name"),
                    })

                output_claims.append({
                "claim": claim_text,
                "status": "fact_checks_found",
                "reviews": reviews,
            })
        else:
            output_claims.append({
                "claim": claim_text,
                "status": "no_fact_check_found",
                "reviews": [],
            })

    return {
        "url": url,
        "claims": output_claims,
    }

@app.post("/analyze")
async def pass_request(request: AnalysisRequest):
    try:
        claims = get_claims(request.url)
        results = get_all_fact_checks(claims)
        response = build_response(request.url, results)
        return response
    except ValueError:
        raise HTTPException(status_code=403, detail="Access is forbidden.")
from fastapi import FastAPI
from factcheck import get_fact_check

'''
app = FastAPI()

@app.get("factchecktools.googleapis.com")
def get_fact_check():
    return get_fact_check
'''

def build_response(url, claims_with_results):
    output_claims = []

    for entry in claims_with_results:

        result = entry["result"]
        claim_text = entry["claim"] #pull data

        if "claims" in entry["result"] and len(entry["result"]["claims"]) > 0: #check if claim exists
            reviews = []
            for matches in result["claims"]:
                for reviews in matches.get("claimReview", []):
                    reviews.append({
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
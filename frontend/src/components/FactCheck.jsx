export default function FactCheck(props) {

    const reviewsArr = props.reviews.map((review, index) => (
        <div className="fact-check-review" key={index}>
            <p className="fact-check-rating">{review.rating}</p>
            <p className="fact-check-publisher">
                <a href={review.url} target="_blank">
                    {review.publisher}
                </a>
            </p>
        </div>
    ))

    return (
        <section className="fact-check-container">
            <h3 className="fact-check-label">Claim</h3>
            <p className="fact-check-claim">{props.claim}</p>
            <div className="fact-check-reviews">
                {reviewsArr}
            </div>
        </section>
    )
}

import React, { useState } from "react"
import FactCheck from "./components/FactCheck"

export default function App() {

    const [checkResults, setCheckResults] = useState([])
    const [urlSubmit, setUrlSubmit] = useState("")
    const [error, setError] = useState(null)

    function isValidUrl(value) {
        try {
            const parsed = new URL(value)
            return parsed.protocol === "http:" || parsed.protocol === "https:"
        } catch {
            return false
        }
    }

    function handleClick() {
        const trimmed = urlSubmit.trim()

        if (!trimmed || !isValidUrl(trimmed)) {
            setError("Please enter a valid URL (including https://).")
            setCheckResults([])
            return
        }

        setError(null)

        fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({url: trimmed})
        })
            .then((response) => response.json())
            .then((data) => {
                setCheckResults(data.claims)
            })
    }

    function handleURLChange(event) {
        setUrlSubmit(event.target.value)
        if (error) setError(null)
    }

    const factChecks = checkResults.filter((check) => check.status === "fact_checks_found").map((check, index) =>
        <FactCheck
            claim={check.claim}
            reviews={check.reviews}
            key={index}
        />
    )

    return (
        <main className="app-main-container">
            <section className="explain-input-container">
                <h1>URL Fact-Checker Tool</h1>
                <p className="explain-lede">Paste a URL to see if fact-checkers have verified the page's contents.</p>
                <p className="explain-note">Note: This only works with articles that have already been fact-checked. As a result, recent news will rarely return fact checks.</p>
                <div className="url-form">
                    <input
                        type="url"
                        id="url-input"
                        name="url"
                        placeholder="https://example.com"
                        value={urlSubmit}
                        onChange={handleURLChange}
                        aria-invalid={Boolean(error)}
                        aria-describedby={error ? "url-error" : undefined}
                    />
                    <button className="submit-button" onClick={handleClick}>Submit</button>
                </div>
                {error && (
                    <p className="form-error" id="url-error" role="alert">
                        {error}
                    </p>
                )}
            </section>
            <section className="fact-check-results">
                {factChecks}
            </section>
        </main>
    )
}
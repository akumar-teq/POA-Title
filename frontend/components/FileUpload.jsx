"use client"

import { useState } from "react"
import api from "../services/api"

export default function FileUpload() {

    const [file, setFile] = useState(null)

    const [result, setResult] = useState(null)

    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    const uploadFile = async () => {

        setLoading(true)
        setError(null)
        setResult(null)

        const formData = new FormData()

        formData.append("file", file)

        try {
            // Upload PDF
            const uploadResponse = await api.post(
                "/upload",
                formData
            )

            // Process PDF
            const processResponse = await api.post(
                "/process",
                {
                    pdf_path:
                        uploadResponse.data.pdf_path
                }
            )

            setResult(processResponse.data)
        } catch (err) {
            setError(err.response?.data?.detail || err.message)
        } finally {
            setLoading(false)
        }
    }

    return (

        <div className="mt-10">

            <input
                type="file"
                onChange={(e) =>
                    setFile(e.target.files[0])
                }
            />

            <button
                onClick={uploadFile}
                disabled={!file || loading}
                className={`text-white px-4 py-2 rounded ml-4 ${(!file || loading) ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500'}`}
            >
                Upload
            </button>

            {loading && (
                <p className="mt-4">
                    Processing document...
                </p>
            )}

            {error && (
                <div className="mt-4 text-red-500 font-bold p-4 bg-red-100 rounded">
                    Error: {error}
                </div>
            )}

            {result && (

                <div className="mt-10 border p-6 rounded">

                    <h2 className="text-2xl font-bold mb-4">
                        OCR Results
                    </h2>

                    <p>
                        <b>Homeowner:</b>
                        {" "}
                        {result.homeowner}
                    </p>

                    <p>
                        <b>Lender:</b>
                        {" "}
                        {result.lender}
                    </p>

                    <p>
                        <b>Loan Amount:</b>
                        {" "}
                        {result.loan_amount}
                    </p>

                    {result.property_address && (
                        <p>
                            <b>Property Address:</b>
                            {" "}
                            {result.property_address}
                        </p>
                    )}

                    {result.county && (
                        <p>
                            <b>County:</b>
                            {" "}
                            {result.county}
                        </p>
                    )}

                    {result.firm_file_no && (
                        <p>
                            <b>Firm File No.:</b>
                            {" "}
                            {result.firm_file_no}
                        </p>
                    )}

                    <p>
                        <b>Risk Level:</b>
                        {" "}
                        {result.risk_level}
                    </p>

                    <a
                        href="http://localhost:8000/report"
                        target="_blank"
                        className="bg-green-500 text-white px-4 py-2 rounded inline-block mt-4"
                    >
                        Download PDF Report
                    </a>

                </div>
            )}

        </div>
    )
}
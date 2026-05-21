"use client"

import { useState } from "react"
import api from "../services/api"

export default function FileUpload() {

    const [file, setFile] = useState(null)

    const [result, setResult] = useState(null)

    const [loading, setLoading] = useState(false)

    const uploadFile = async () => {

        setLoading(true)

        const formData = new FormData()

        formData.append("file", file)

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

        setLoading(false)
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
                className="bg-blue-500 text-white px-4 py-2 rounded ml-4"
            >
                Upload
            </button>

            {loading && (
                <p className="mt-4">
                    Processing document...
                </p>
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
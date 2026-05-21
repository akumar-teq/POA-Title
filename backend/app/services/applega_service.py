def upload_document(file_path, matter_id):

    print("Mock Upload Started")

    print(f"Uploading: {file_path}")

    print(f"Matter ID: {matter_id}")

    return {
        "status": "success",
        "message": "Mock upload completed"
    }


def update_matter_status(
    matter_id,
    status
):

    print("Mock Status Update")

    print(f"Matter ID: {matter_id}")

    print(f"Status: {status}")

    return {
        "status": "success"
    }
import base64

def image_to_base64(uploaded_file):
    """
    Converts an uploaded Streamlit file into a base64 string 
    so it can be embedded in HTML with full quality.
    """
    try:
        bytes_data = uploaded_file.getvalue()
        b64_str = base64.b64encode(bytes_data).decode()
        # Determine mime type (default to png if unknown)
        mime_type = uploaded_file.type if uploaded_file.type else "image/png"
        return f"data:{mime_type};base64,{b64_str}"
    except Exception as e:
        return None
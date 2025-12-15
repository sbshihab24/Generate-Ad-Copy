import streamlit as st
from backend.ai_service import generate_ad_copy

# Helper for image conversion
try:
    from backend.utils import image_to_base64
except ImportError:
    def image_to_base64(file): return None

def render_app():
    st.title("Create Your Ad")
    st.caption("Upload creative assets and write compelling ad copy")

    # --- Create Two Main Columns ---
    # Left (Inputs) and Right (Preview)
    left_col, right_col = st.columns([1.5, 1], gap="large")

    # ==========================
    # LEFT COLUMN: Inputs
    # ==========================
    with left_col:
        st.subheader("Ad Details", anchor=False)
        st.text_input("Ad Name", placeholder="e.g., Summer Sale 2025")
        
        st.write("Ad Format")
        c1, c2 = st.columns(2)
        with c1: st.button("🖼️ Image Ad", use_container_width=True, type="primary")
        with c2: st.button("🎥 Video Ad", use_container_width=True)

        st.markdown("---")

        st.subheader("Upload Creative", anchor=False)
        uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg", "mp4"])

        st.markdown("---")

        st.subheader("Generate Ad Copy", anchor=False)
        product_service = st.text_input("Product/Service", placeholder="e.g., Sneakers")
        target_audience = st.text_input("Target Audience", placeholder="e.g., Students")
        key_benefits = st.text_input("Key Benefits", placeholder="Comfortable, stylish...")
        tone = st.selectbox("Tone", ["Professional", "Friendly", "Urgent", "Luxury", "Witty"])

        if st.button("✨ Generate Copy", type="primary", use_container_width=True):
            if not product_service or not target_audience:
                st.warning("Please enter Product & Audience.")
            else:
                with st.spinner("Writing your ad..."):
                    result = generate_ad_copy(product_service, target_audience, key_benefits, tone)
                    if "error" in result:
                        st.error(result['error'])
                    else:
                        st.session_state['gen_headline'] = result.get('headline', '')
                        st.session_state['gen_primary'] = result.get('primary_text', '')
                        st.session_state['gen_desc'] = result.get('description', '')
                        st.session_state['gen_cta'] = result.get('call_to_action', 'Learn More')

        st.markdown("---")

        st.subheader("Edit Content", anchor=False)
        headline = st.text_input("Headline", value=st.session_state.get('gen_headline', ''))
        primary_text = st.text_area("Primary Text", value=st.session_state.get('gen_primary', ''), height=150)
        description = st.text_input("Description", value=st.session_state.get('gen_desc', ''))
        cta = st.selectbox("Call to Action", ["Learn More", "Shop Now", "Sign Up"], index=0)

    # ==========================
    # RIGHT COLUMN: Ad Preview
    # ==========================
    with right_col:
        st.subheader("Ad Preview", anchor=False)
        
        # A. Prepare Image
        img_html = ""
        if uploaded_file:
            b64 = image_to_base64(uploaded_file)
            if b64:
                img_html = f'<img src="{b64}" alt="Ad" style="width:100%; display:block;">'
        
        if not img_html:
            img_html = '<div style="height:300px; background:#F0F2F5; display:flex; align-items:center; justify-content:center; color:#888; font-size:40px;">🖼️</div>'

        # B. Prepare Text
        d_head = headline if headline else "Headline Here"
        d_prim = primary_text if primary_text else "Primary text will appear here..."
        d_desc = description if description else ""

        # C. Render Card (NO INDENTATION in the string below to fix the bug)
        html_code = f"""
<div style="margin-top: 20px;">
<div class="ad-preview-card">
<div class="ad-header">
<div class="profile-icon"></div>
<div class="ad-header-text">
<h4>Your Page Name</h4>
<span>Sponsored • <i style="font-style:normal">🌍</i></span>
</div>
</div>
<div class="ad-primary-text">{d_prim}</div>
<div class="ad-image-container">{img_html}</div>
<div class="ad-footer">
<div class="ad-domain">WEBSITE.COM</div>
<div class="ad-headline">{d_head}</div>
<div class="ad-description">{d_desc}</div>
<div class="ad-cta-button">{cta}</div>
</div>
</div>
</div>
"""
        st.markdown(html_code, unsafe_allow_html=True)
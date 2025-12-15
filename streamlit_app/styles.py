import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* General App Background */
        .stApp { background-color: #F0F2F5; }

        /* --- PREVIEW CARD STYLING --- */
        .ad-preview-card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
            border: 1px solid #ddd;
            overflow: hidden;
            font-family: Helvetica, Arial, sans-serif;
            max-width: 400px; /* Limits width to look like a phone/feed */
            margin: 0 auto;   /* Centers the card */
        }

        /* Header (Profile Pic + Name) */
        .ad-header {
            padding: 12px;
            display: flex;
            align-items: center;
        }
        .profile-icon {
            width: 40px;
            height: 40px;
            background-color: #ccc;
            border-radius: 50%;
            margin-right: 10px;
        }
        .ad-header-text h4 {
            margin: 0;
            font-size: 14px;
            font-weight: 600;
            color: #1c1e21;
        }
        .ad-header-text span {
            font-size: 12px;
            color: #65676B;
        }

        /* Primary Text */
        .ad-primary-text {
            padding: 0 12px 12px 12px;
            font-size: 14px;
            color: #1c1e21;
            line-height: 1.4;
        }

        /* The Ad Image (High Quality) */
        .ad-image-container img {
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover; /* Ensures it fills space nicely */
        }

        /* Footer (Headline + CTA) */
        .ad-footer {
            padding: 10px 12px;
            background-color: #F0F2F5; /* Light gray bottom area like some FB ads */
            border-top: 1px solid #e5e5e5;
        }
        .ad-domain {
            font-size: 12px;
            color: #65676B;
            margin-bottom: 2px;
            text-transform: uppercase;
        }
        .ad-headline {
            font-size: 16px;
            font-weight: 700;
            color: #1c1e21;
            margin-bottom: 4px;
            line-height: 1.2;
        }
        .ad-description {
            font-size: 13px;
            color: #65676B;
            margin-bottom: 12px;
            display: -webkit-box;
            -webkit-line-clamp: 3; /* CHANGED FROM 1 TO 3 */
            -webkit-box-orient: vertical;
            overflow: hidden;
            line-height: 1.4;      /* Added for better readability */
        }

        /* The "Learn More" Button */
        .ad-cta-button {
            display: block;
            width: 100%;
            text-align: center;
            background-color: #EBF5FF; /* Light blue background */
            color: #0064D1; /* Facebook Blue text */
            font-weight: 600;
            padding: 10px 0;
            border-radius: 6px;
            text-decoration: none;
            margin-top: 5px;
            cursor: pointer;
        }
        .ad-cta-button:hover {
            background-color: #DCEFFF;
        }
        </style>
    """, unsafe_allow_html=True)
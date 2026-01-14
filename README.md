# Ad Creator Portal

## Project Overview

The **Ad Creator Portal** is an intelligent web application that helps users create professional, high-converting advertisement copy and preview ads in a Facebook/Instagram feed format. It leverages OpenAI's GPT-4 model to generate compelling ad content based on user inputs and provides real-time preview of how ads will appear on social media platforms.

---

## Key Features

### 🎨 **AI-Powered Ad Copy Generation**
- Uses OpenAI's GPT-4 model to generate high-quality ad copy
- Supports multiple tone variations: Professional, Friendly, Urgent, Luxury, and Witty
- Generates four essential components:
  - **Headline**: Powerful, attention-grabbing hook (max 50 characters)
  - **Primary Text**: Main body of the ad (max 300 characters)
  - **Description**: Persuasive link description with social proof (max 150 characters)
  - **Call-to-Action**: Optimized button text (Learn More, Shop Now, Sign Up, etc.)

### 📸 **Creative Asset Support**
- Upload image files (PNG, JPG, JPEG) or video assets (MP4)
- Base64 encoding for seamless image preview and embedding
- Support for both Image Ads and Video Ads formats

### 👁️ **Live Ad Preview**
- Real-time preview of ads in a Facebook/Instagram feed format
- Authentic styling with profile headers, sponsored labels, and call-to-action buttons
- Responsive design that simulates mobile feed appearance
- High-quality image rendering with proper formatting

### ✏️ **Content Editing**
- Edit generated ad content directly in the interface
- Fine-tune headlines, primary text, descriptions, and CTAs
- Custom tone selection for different marketing strategies

### 🎯 **Tone-Based Generation**
- **Professional**: Formal, trust-building language focused on value and efficiency
- **Friendly**: Conversational, warm tone with relatable language
- **Urgent**: Short, punchy sentences with FOMO-inducing copy
- **Luxury**: Sophisticated vocabulary emphasizing exclusivity and premium quality
- **Witty**: Clever, playful, humorous approach with wordplay

---

## Project Structure

```
create_your_ad/
├── app.py                    # Main Streamlit application entry point
├── requirements.txt          # Python dependencies
├── .env                       # Environment variables (API keys)
├── .gitignore                # Git ignore rules
├── .venv/                     # Virtual environment (local)
├── backend/
│   ├── __init__.py           # Package initialization
│   ├── ai_service.py         # OpenAI API integration and copy generation
│   └── utils.py              # Utility functions (image encoding, etc.)
└── streamlit_app/
    ├── __init__.py           # Package initialization
    ├── layout.py             # UI layout and components
    └── styles.py             # Custom CSS styling for the application
```

### File Descriptions

#### **app.py**
- Entry point for the Streamlit application
- Loads environment variables from `.env` file
- Configures page settings (title: "Ad Creator Portal", layout: "wide")
- Applies custom styling and renders the main application layout

#### **backend/ai_service.py**
- Initializes OpenAI client with secure API key management
- **Key Function**: `generate_ad_copy(product_service, target_audience, key_benefits, tone)`
  - Generates structured JSON output with headline, primary text, description, and CTA
  - Uses advanced prompt engineering with tone-specific instructions
  - Temperature: 0.75 for balanced creativity and consistency
  - Model: GPT-4o for high-quality output

#### **backend/utils.py**
- **Key Function**: `image_to_base64(uploaded_file)`
  - Converts uploaded Streamlit files to base64 encoding
  - Enables high-quality embedding of images in HTML preview
  - Supports PNG, JPG, JPEG, and other image formats

#### **streamlit_app/layout.py**
- Builds the main UI with two-column layout:
  - **Left Column**: Input controls and ad generation interface
  - **Right Column**: Live ad preview
- Handles:
  - Ad naming and format selection
  - File uploads for creative assets
  - Ad copy generation via user inputs
  - Content editing fields
  - Real-time preview rendering

#### **streamlit_app/styles.py**
- Custom CSS styling for authentic Facebook/Instagram ad appearance
- Defines styling for:
  - Preview card layout and shadows
  - Profile icon and header styling
  - Ad image containers with proper scaling
  - Footer with domain, headline, description, and CTA button
  - Light gray background (#F0F2F5) for authentic social media feel

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (from https://platform.openai.com/api-keys)
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd create_your_ad
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On macOS/Linux
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | Latest | Web UI framework for data applications |
| `openai` | Latest | OpenAI API client for GPT-4 integration |
| `python-dotenv` | Latest | Environment variable management |

---

## Usage Guide

### Creating an Ad

1. **Enter Ad Details**
   - Provide a name for your ad campaign
   - Choose between Image Ad or Video Ad format

2. **Upload Creative Assets**
   - Upload an image (PNG, JPG, JPEG) or video (MP4)
   - Asset will be displayed in the preview card

3. **Generate Ad Copy**
   - Fill in:
     - **Product/Service**: What you're advertising (e.g., "Premium Sneakers")
     - **Target Audience**: Who you're targeting (e.g., "College Students")
     - **Key Benefits**: Main selling points (e.g., "Comfortable, Stylish, Durable")
     - **Tone**: Select the desired tone from the dropdown
   - Click "✨ Generate Copy" button

4. **Review and Edit**
   - AI-generated content appears in editable fields
   - Customize any field to match your brand voice
   - Live preview updates in real-time

5. **Monitor Preview**
   - Right column shows exact ad appearance on social media
   - Verify headline, primary text, description, and CTA

---

## API Integration

### OpenAI Integration

The application uses **OpenAI's GPT-4o model** with the following configuration:

- **Model**: `gpt-4o` (recommended for high-quality output)
- **Temperature**: 0.75 (balanced between creativity and consistency)
- **Response Format**: JSON object with strict schema validation
- **Max Tokens**: Default (sufficient for ad copy)

### Error Handling

- Missing API key: Returns "OpenAI API Key not found" error
- API failures: Caught and displayed to user with error message
- Invalid inputs: Validation checks in the UI

---

## Technical Architecture

### Frontend (Streamlit)
- **Framework**: Streamlit (Python-based web framework)
- **Layout**: Two-column responsive design
- **State Management**: Streamlit session state for persisting generated content
- **Styling**: Custom CSS with HTML injection

### Backend (Python)
- **AI Service**: OpenAI API integration with prompt engineering
- **Utilities**: Image processing and encoding
- **Configuration**: Environment-based secrets management

### Data Flow
```
User Input (Product, Audience, Benefits, Tone)
        ↓
generate_ad_copy() function
        ↓
OpenAI GPT-4 API Call
        ↓
JSON Response Processing
        ↓
Store in Session State
        ↓
Live Preview Rendering
```

---

## Customization

### Modifying Tone Instructions
Edit `backend/ai_service.py` in the `tone_instructions` dictionary to add custom tones:
```python
tone_instructions = {
    "Your_Tone": "Your custom tone instructions here..."
}
```

### Adjusting Styling
Edit `streamlit_app/styles.py` to customize:
- Colors and fonts
- Card dimensions and shadows
- Responsive behavior
- Button styles

### Changing AI Model
Edit `backend/ai_service.py` line with `model="gpt-4o"` to use:
- `gpt-4-turbo` for faster responses
- `gpt-3.5-turbo` for budget optimization (lower quality)

---

## Troubleshooting

### Issue: "OpenAI API Key not found"
**Solution**: Ensure `.env` file exists in the project root with valid `OPENAI_API_KEY`

### Issue: Image not displaying in preview
**Solution**: 
- Verify file format is PNG, JPG, or JPEG
- Check file size (recommend < 5MB)
- Ensure file upload completed successfully

### Issue: Streamlit app not starting
**Solution**:
- Verify all dependencies installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (3.8+)
- Run with verbose mode: `streamlit run app.py --logger.level=debug`

### Issue: Generated copy is too short or generic
**Solution**:
- Increase temperature in `ai_service.py` (0.75 → 0.85)
- Provide more detailed "Key Benefits"
- Try different tone selections
- Verify you're using GPT-4o model (not gpt-3.5-turbo)

---

## Security Considerations

1. **API Key Management**
   - Never commit `.env` file to version control
   - Use `.gitignore` to exclude sensitive files
   - Rotate API keys periodically

2. **File Uploads**
   - Validate file types (currently accepts PNG, JPG, JPEG, MP4)
   - Consider adding file size limits

3. **Data Privacy**
   - Ad copy content is sent to OpenAI for processing
   - Review OpenAI's data retention policy

---

## Performance Optimization

- **Caching**: Consider implementing Streamlit's @st.cache decorator for API calls
- **Model Selection**: Use `gpt-3.5-turbo` for faster responses in production
- **Image Processing**: Base64 encoding is efficient for web display

---

## Future Enhancement Ideas

- [ ] Multi-language ad generation support
- [ ] A/B testing interface for comparing different ad variations
- [ ] Ad performance analytics dashboard
- [ ] Integration with Facebook/Instagram APIs for direct posting
- [ ] Batch ad generation for multiple products
- [ ] Custom brand voice templates
- [ ] Ad approval workflow with team collaboration
- [ ] Analytics on which tones perform best

---

## Contributing

To contribute to this project:
1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request with description

---

## License

This project is part of the AdPortal Platform Website collection.

---

## Support

For issues, questions, or suggestions:
- Check the Troubleshooting section above
- Review OpenAI API documentation: https://platform.openai.com/docs
- Check Streamlit documentation: https://docs.streamlit.io

---

## Project Metadata

- **Created**: January 2025
- **Technology Stack**: Python, Streamlit, OpenAI GPT-4
- **Purpose**: AI-powered advertisement creation and preview
- **Status**: Active Development

---

## Version History

### v1.0 (Current)
- Initial release
- AI-powered ad copy generation with multiple tones
- Image/Video upload support
- Live social media preview
- Custom styling
- Session state management

---

## Author & Contact

**Shihab**

🔗 **Portfolio**: [https://shihab247.netlify.app/](https://shihab247.netlify.app/)

🔗 **GitHub**: [https://github.com/sbshihab24](https://github.com/sbshihab24)

🔗 **LinkedIn**: [https://www.linkedin.com/in/shihab24](https://www.linkedin.com/in/shihab24)

📧 **Email**: sbshihab2000@gmail.com

📱 **Phone**: +880 1790606985

Feel free to reach out for collaborations, questions, or project inquiries!


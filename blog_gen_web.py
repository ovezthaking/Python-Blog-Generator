import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Generator Blogów AI",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize OpenAI client
@st.cache_resource
def init_openai_client():
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv('OPENAI_API_KEY'),
    )

def generate_blog(paragraph_topic):
    """Generate blog content using OpenAI API"""
    client = init_openai_client()
    
    try:
        completion = client.chat.completions.create(
            extra_headers={},
            extra_body={},
            model="openai/gpt-oss-20b:free",
            messages=[
                {
                    "role": "user",
                    "content": 'Write a paragraph about the following topic. ' + paragraph_topic,
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Błąd podczas generowania treści: {str(e)}"

# Main Streamlit interface
def main():
    # Header
    st.title("📝 Generator Blogów AI")
    st.markdown("---")
    
    # Description
    st.markdown("""
    Witaj w generatorze blogów opartym na sztucznej inteligencji! 
    Wprowadź temat, a AI wygeneruje dla Ciebie ciekawy akapit.
    """)
    
    # Input section
    st.subheader("🎯 Wprowadź temat")
    topic = st.text_area(
        label="Temat do napisania akapitu:",
        placeholder="Np. Ciekawostki o Pieńsku - Małym mieście na Dolnym Śląsku",
        height=100,
        help="Opisz temat, o którym chcesz, żeby AI napisało akapit"
    )
    
    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_button = st.button("🚀 Wygeneruj Blog", type="primary", use_container_width=True)
    
    # Generation and display
    if generate_button:
        if topic.strip():
            # Show loading spinner
            with st.spinner('Generuję treść... To może potrwać chwilę.'):
                generated_content = generate_blog(topic.strip())
            
            # Display results
            st.markdown("---")
            st.subheader("📄 Wygenerowana treść")
            
            # Content container with styling
            st.markdown(
                f"""
                <div style="
                    background-color: #f0f2f6;
                    padding: 20px;
                    border-radius: 10px;
                    border-left: 4px solid #1f77b4;
                    margin: 10px 0;
                ">
                    <p style="font-size: 16px; line-height: 1.6; color: #333;">
                        {generated_content}
                    </p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Copy button
            st.code(generated_content, language=None)
            st.success("✅ Treść została wygenerowana pomyślnie!")
            
        else:
            st.error("⚠️ Proszę wprowadź temat przed generowaniem!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 14px;">
        Powered by OpenAI via OpenRouter | Made with ❤️ using Streamlit
    </div>
    """, unsafe_allow_html=True)

# Sidebar with additional info
def sidebar():
    st.sidebar.title("ℹ️ Informacje")
    st.sidebar.markdown("""
    **Jak korzystać:**
    1. Wprowadź temat w polu tekstowym
    2. Kliknij "Wygeneruj Blog"
    3. Skopiuj wygenerowaną treść
    
    **Wskazówki:**
    - Bądź konkretny w opisie tematu
    - Możesz używać polskich znaków
    - Im bardziej szczegółowy temat, tym lepsza treść
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.info("💡 **Tip:** Jeśli wystąpi błąd kwoty (quota), sprawdź swoje konto OpenAI!")

if __name__ == "__main__":
    sidebar()
    main()

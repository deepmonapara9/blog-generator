# Blog Generator

Blog Generator is a Django-based web application that leverages PostgreSQL for database management, Supabase for authentication and real-time subscriptions, AssemblyAI for transcription services, and OpenAI API for blog generation.

## Features

- **PostgreSQL Database:** Utilize PostgreSQL for database management.
- **Supabase Integration:** Utilize Supabase for authentication and real-time subscriptions.
- **AssemblyAI Transcription:** Seamlessly transcribe audio files into text using AssemblyAI's powerful speech-to-text API.
- **OpenAI Blog Generation:** Generate high-quality blog content using OpenAI's language model.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/blog-generator.git
   cd blog-generator
   
2. Install dependencies:
   
     pip install -r requirements.txt

3. Set up PostgreSQL:
   
   Install PostgreSQL on your system if not already installed. <br>
   Create a new database and user with appropriate permissions.<br>
   Update the DATABASES configuration in settings.py with your PostgreSQL database credentials.<br>

4. Set up Supabase:

   Sign up for a free account on Supabase.<br>
   Create a new project and obtain your API URL and public key.<br>
   Update the DATABASES configuration in settings.py with your Supabase credentials.<br>

5. Configure AssemblyAI:

   Sign up for an account on AssemblyAI.<br>
   Obtain your API key.<br>
   Update the ASSEMBLYAI_API_KEY variable in settings.py with your AssemblyAI API key.<br>

6. Set up OpenAI API:

   Sign up for an account on OpenAI.<br>
   Obtain your API key.<br>
   Update the OPENAI_API_KEY variable in settings.py with your OpenAI API key.<br>

7. Run migrations:

   python manage.py migrate

8. Run the development server:

   python manage.py runserver

9. Access the application at http://localhost:8000.


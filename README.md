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

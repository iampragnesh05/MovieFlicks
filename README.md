<h1 style="text-align:center; font-family:Arial, sans-serif; color:#2C3E50;">MovieFlicks</h1>

<p style="text-align:center; font-size:16px; color:#7F8C8D;">A dynamic movie-ranking application powered by Flask and TMDb API.</p>

<hr style="border: 1px solid #ecf0f1;">

<h2 style="color:#34495E;">Overview</h2>
<p style="font-size:14px; line-height:1.6; color:#2C3E50;">
<strong>MovieFlicks</strong> is a web application where users can create and manage their personalized top 10 movie list. It integrates with The Movie Database (TMDb) API to search and fetch movie details, providing an interactive and dynamic movie ranking experience.
</p>

<h2 style="color:#34495E;">Features</h2>
<ul style="color:#2C3E50; line-height:1.8;">
  <li>Add movies by searching via title using TMDb API.</li>
  <li>Select the correct movie when multiple results are returned.</li>
  <li>Update movie ratings and reviews with an intuitive UI.</li>
  <li>Dynamic rankings based on ratings, automatically updating order.</li>
  <li>Delete movies with a single click.</li>
  <li>Responsive design with Bootstrap for enhanced user experience.</li>
</ul>

<h2 style="color:#34495E;">Technologies Used</h2>
<ul style="color:#2C3E50; line-height:1.8;">
  <li><strong>Backend:</strong> Flask, SQLAlchemy</li>
  <li><strong>Frontend:</strong> Jinja2, Bootstrap</li>
  <li><strong>Database:</strong> SQLite</li>
  <li><strong>API Integration:</strong> TMDb API</li>
  <li><strong>Environment Management:</strong> python-dotenv</li>
  <li><strong>Version Control:</strong> Git and GitHub</li>
</ul>


<h2 style="color:#34495E;">Setup Instructions</h2>
<ol style="color:#2C3E50; line-height:1.8;">
  <li>Clone the repository:</li>
  <pre style="background-color:#ecf0f1; padding:10px; border-radius:5px; font-size:13px;">git clone https://github.com/yourusername/MovieFlicks.git</pre>
  <li>Create and activate a virtual environment:</li>
  <pre style="background-color:#ecf0f1; padding:10px; border-radius:5px; font-size:13px;">python -m venv venv<br>source venv/bin/activate</pre>
  <li>Install dependencies:</li>
  <pre style="background-color:#ecf0f1; padding:10px; border-radius:5px; font-size:13px;">pip install -r requirements.txt</pre>
  <li>Create a <code>.env</code> file and add your TMDb API key:</li>
  <pre style="background-color:#ecf0f1; padding:10px; border-radius:5px; font-size:13px;">api_key=YOUR_TMDB_API_KEY</pre>
  <li>Initialize the database:</li>
  <pre style="background-color:#ecf0f1; padding:10px; border-radius:5px; font-size:13px;">python<br>>> from app import db<br>>> db.create_all()<br>>> exit()</pre>
  <li>Run the application:</li>
  <pre style="background-color:#ecf0f1; padding:10px; border-radius:5px; font-size:13px;">flask run</pre>
  <li>Visit the application at <a href="http://127.0.0.1:5000" style="color:#3498DB;">http://127.0.0.1:5000</a>.</li>
</ol>

<h2 style="color:#34495E;">What I Learned</h2>
<ul style="color:#2C3E50; line-height:1.8;">
  <li>How to build a Flask web application with CRUD operations.</li>
  <li>Integrating third-party APIs to fetch real-time data.</li>
  <li>Implementing dynamic data management with SQLAlchemy ORM.</li>
  <li>Creating user-friendly interfaces with Bootstrap and Jinja2 templates.</li>
  <li>Handling version control with Git and GitHub.</li>
</ul>

<h2 style="color:#34495E;">Future Enhancements</h2>
<ul style="color:#2C3E50; line-height:1.8;">
  <li>Implement user authentication for personalized lists.</li>
  <li>Add search and filter functionality for the movie list.</li>
  <li>Include a "Watch Trailer" feature using YouTube API.</li>
  <li>Enhance UI/UX with modern design elements.</li>
</ul>


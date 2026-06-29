# Interactive Web Invitation

A full-stack web application designed as a digital wedding invitation featuring a subtle theme inspired by *The Legend of Zelda*. This project allows guests to view event details, interact with the interface, and confirm their attendance via an automated system connected to a database.

## Core Features

* **Themed UI/UX:** Elegant interface styled with green and gold tones, classical typography (Cinzel and Cormorant Garamond), and visual details referencing the Zelda saga (Triforce and custom buttons).
* **Particle Effects:** Custom-configured integration of particles.js to simulate floating magical dust or "Hyrule Fairies" in the background (optimized without connecting lines for a cleaner appearance).
* **Immersive Audio:** Integrated web audio player allowing guests to play or pause background music (Zelda's Lullaby), compliant with modern browser autoplay policies via a floating toggle button.
* **Modal Navigation System (SPA):** Fluid single-page navigation utilizing modal windows to display:
  * **Locations:** Embedded maps for both the ceremony and reception venues.
  * **Gift Registry:** External redirection links to commercial platforms.
  * **RSVP Confirmation:** Data capture form.
* **Secure Registration System:** Backend configured to process POST requests from the RSVP form, featuring pre-validation logic that queries the database to prevent duplicate registrations from the same guest.

## Tech Stack

**Frontend:**
* HTML5 / CSS3 (Responsive design, Flexbox, CSS variables, z-index layering).
* JavaScript (Vanilla JS for DOM manipulation, modal handling, and Audio object control).
* particles.js (External library loaded via CDN).

**Backend & Data:**
* Python 3: Core server-side application logic.
* Flask: Web micro-framework utilized for routing (@app.route) and rendering views (render_template).
* SQLite: Lightweight relational database (boda.db) for persistent guest storage.

## Directory Architecture

The project adheres to the standard Flask application structure:

```text
BODAZELDA/
│
├── app.py                 # Main Flask server script and routing
├── boda.db                # SQLite database (Table: guests)
│
├── templates/             
│   └── index.html         # Core structure, modals, and audio player
│
└── static/                # Public static files
    ├── index.css          # Stylesheets and custom properties
    ├── index.js           # Client-side logic and particle configuration
    ├── lullaby.mp3        # Ambient background audio track
    └── img/
        ├── esquina.png    # Decorative corner ornaments
        └── trifuerza.png  # Central Triforce logo

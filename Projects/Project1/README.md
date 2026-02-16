# Student Portfolio Web Application

A modern, responsive Python Flask web application for showcasing a student's portfolio with three main pages: Home, Previous Semester, and Portfolio.

## Features

### 🎨 Modern Design
- **Advanced CSS**: Custom animations, gradients, and transitions
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile devices
- **Dark Theme**: Eye-friendly dark color scheme with vibrant accent colors

### 📱 Navigation
- **Fixed Navbar**: Always accessible navigation bar with smooth transitions
- **Mobile Menu**: Hamburger menu for mobile devices with slide-in animation
- **Active Link Highlighting**: Shows the current page in navigation

### 🏠 Home Page
- Hero section with animated floating card
- About Me section with skills grid
- Animated statistics counter
- Interactive scroll animations
- Call-to-action buttons

### 📚 Previous Semester Page
- Semester overview with GPA badge
- Course cards with grades and topics
- Interactive timeline of semester highlights
- Detailed course descriptions

### 💼 Portfolio Page
- Project showcase grid with category filtering
- Project cards with hover effects and overlays
- Technical skills section with animated progress bars
- Tag-based project categorization

### ✨ Animations
- Fade-in animations on scroll
- Floating elements
- Smooth hover transitions
- Progress bar animations
- Counter animations
- Glowing effects

## Technologies Used

- **Backend**: Python Flask 3.0.0
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Icons**: Font Awesome 6.4.0
- **Server**: Werkzeug 3.0.1

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd "/Users/ragnar/Documents/COD LANG/FTW/Projects/Project1"
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python autoRefreshTime.py
   ```

2. **Access the application**:
   - Open your web browser
   - Navigate to: `http://localhost:5001`
   - Or access from other devices on the same network: `http://YOUR_IP:5001`

The server runs in debug mode, which means:
- Automatic reloading on code changes
- Detailed error messages
- Available on all network interfaces (0.0.0.0)

## Project Structure

```
Project1/
│
├── main.py                 # Flask application entry point
├── requirements.txt        # Python dependencies
│
├── templates/             # HTML templates
│   ├── base.html         # Base template with navbar and footer
│   ├── home.html         # Home page
│   ├── previous_semester.html  # Previous Semester page
│   └── portfolio.html    # Portfolio page
│
└── static/               # Static assets
    └── css/
        └── style.css     # Main stylesheet with animations
```

## Pages Overview

### 1. Home (`/`)
The landing page features:
- Eye-catching hero section
- About section with skill highlights
- Animated statistics
- Call-to-action buttons

### 2. Previous Semester (`/previous-semester`)
Academic achievements page with:
- Semester overview and GPA
- Course cards with grades and topics
- Timeline of key events
- Detailed course information

### 3. Portfolio (`/portfolio`)
Projects showcase featuring:
- Filterable project grid
- Project cards with descriptions
- Technical skills with progress bars
- Category-based filtering (All, Web, Python, Data Science)

## Customization

### Colors
Edit CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #6366f1;
    --secondary-color: #8b5cf6;
    --accent-color: #ec4899;
    /* ... more colors */
}
```

### Content
- **Home page**: Edit `templates/home.html`
- **Previous Semester**: Edit `templates/previous_semester.html`
- **Portfolio**: Edit `templates/portfolio.html`

### Styling
All styles are in `static/css/style.css` with clear section comments.

## Responsive Breakpoints

- **Desktop**: > 968px
- **Tablet**: 576px - 968px
- **Mobile**: < 576px

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Features Details

### Animations
- Scroll-triggered fade-in effects
- Floating elements
- Counter animations
- Progress bar fills
- Smooth transitions
- Hover effects

### Interactivity
- Project filtering by category
- Mobile menu toggle
- Smooth scrolling
- Active navigation highlighting
- Responsive layout adjustments

## Development

To make changes:
1. Edit files as needed
2. Save changes (Flask auto-reloads in debug mode)
3. Refresh browser to see updates

## Credits

- Font Awesome for icons
- Flask framework
- Modern CSS3 features

## License

This is a student portfolio project created for educational purposes.

---

**Note**: The application runs on port 5001 to avoid conflicts with macOS AirPlay Receiver, which uses port 5000.

Enjoy your modern student portfolio website! 🚀

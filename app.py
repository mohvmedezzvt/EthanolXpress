from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Predefined list of blogs (can be replaced with actual blog content)
blogs = [
    { 'id': 1, 'title': 'Ethanol for saving energy and protecting the environment', 'content': 'Content of Blog Post 1...' },
    { 'id': 2, 'title': 'Factory Waste for Ethanol Production', 'content': 'Content of Blog Post 2...' },
    { 'id': 3, 'title': 'Utilizing Bioprocessing for Low-Cost Ethanol Extraction from Factory Waste', 'content': 'Content of Blog Post 3...' },
    { 'id': 4, 'title': 'Exploring Bioethanol as a Sustainable Solution for Future Energy Needs', 'content': 'Content of Blog Post 4...' },
    { 'id': 5, 'title': 'Ethanol vs. Gasoline: A Comparison of Benefits and Risks', 'content': 'Content of Blog Post 5...' },
    { 'id': 6, 'title': 'Ethanol as an Alternative to Traditional Fuel', 'content': 'Content of Blog Post 6...' }
]

@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html', blogs=blogs)


@app.route('/blog', strict_slashes=False)
def blog():
    blog_id = request.args.get('blog_id')
    blog = next((b for b in blogs if str(b['id']) == blog_id), None)
    if blog:
        return render_template('blog.html', blog=blog)
    else:
        return 'Blog not found', 404



if __name__ == '__main__':
    app.run(debug=True)

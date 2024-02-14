# Mini Challenge 1

## Create the pages app

### Acceptance Criteria

1. Create a HomePageView in `pages/views.py` that renders a template called `pages/home.html`.
2. Create an AboutPageView in `pages/views.py` that renders the template `pages/about.html`.
3. Create a `urls.py` file within your pages app that resolves both:
   3.1. HomePageView
   3.2. AboutPageView
4. Create a templates directory with a `pages` subdirectory with at least these 2 templates:
   4.1. `home.html`
   4.2. `about.html`
5. Create a `base.html` template in your `templates` directory (parent template)
6. Add bootstrap support to your base template which is inherited in all child templates
7. Add a navbar with links to both home and about (pages).
8. Modify `config/urls.py` to _include_ a reference to `pages.urls`.

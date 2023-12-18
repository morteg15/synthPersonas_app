# blueprints/auth/views.py
from flask import render_template, request, session, redirect, url_for, flash
from . import auth_blueprint

@auth_blueprint.route('/get-api-key', methods=['GET', 'POST'])
def get_api_key():
    if request.method == 'POST':
        api_key = request.form.get('api_key')
        if api_key:
            # Save the API key
            session['api_key'] = api_key
            flash('API Key saved successfully.', 'success')
            return redirect(url_for('selection.selection'))  # Redirect to the landing page
        else:
            flash('Please enter an API Key.', 'error')
    
    return render_template('auth/get_api_key.html')
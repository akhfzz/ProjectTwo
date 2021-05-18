from __init__ import app
from models import User, Komunitas, EBook 
from passlib.hash import sha256_crypt
from flask import Flask, flash, render_template, session, current_app, send_from_directory, redirect, request, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
from flask_paginate import Pagination, get_page_parameter

@app.route('/')
def visitors():
	return render_template('visitors.html')

@login_required
@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)

@app.route('/publicPost', methods=['POST', 'GET'])
def public():
	book = EBook()
	getId = book.selectRelation()
	return render_template("publik.html", ebook=getId)

@login_required
@app.route('/profil', methods=['POST', 'GET'])
def index():
	iduser = session['id']
	username = session['username']
	book = EBook()
	getId = book.selectEBook(iduser)
	user = User()
	data = user.LoginPDB(username)
	if request.method == 'POST':
		judul = request.form['judul']
		tahun = request.form['tahun']
		tipe = request.form['type']
		file = request.files['file']
		data = (judul, tahun, tipe, secure_filename(file.filename), iduser)
		filename = app.config['UPLOAD_FOLDER'] + '/' + secure_filename(file.filename)
		buku = EBook()
		buku.InsertDB(data)
		try:
			file.save(filename)
			flash('File Success Uploaded', 'success')
			return render_template('User.html',username=username,data=data, filename=secure_filename(file.filename), check=getId, iduser=iduser)
		except:
			flash('There is problem with our server', 'info')
			return render_template('User.html', username=username, check=getId, iduser=iduser, data=data)
	return render_template('User.html', username=username, iduser=iduser, check=getId, data=data)

@login_required
@app.route("/logout")
def logout():
	# session.pop("user", None)
	logout_user()
	flash(f"You've logout","success")
	return redirect(url_for('visitors'))

@login_required
@app.route("/delete", methods=['POST', 'GET'])
def delete():
	if request.method == 'POST':
		book = EBook()
		all_data = book.selectAll()[0][1]
		book.deleteDB(all_data)
		flash("File's been deleted", "info")
		return redirect(url_for('index'))

# @login_required
# @app.route('/deletes', methods=['POST', 'GET'])
# def deleted():
# 	if request.method == 'POST':
# 		company = Komunitas()
# 		all_data = company.selectAllDB()[0][0]
# 		company.deleteDB(all_data)
# 		return redirect(url_for('community'))

@app.route('/register', methods=['POST', 'GET'])
def formRegister():
	user = User()
	if request.method == 'POST':
		username = request.form['namaUser']
		email = request.form['email']
		psw = request.form['password']
		secure = sha256_crypt.encrypt(str(psw))
		data = [username, secure, email]
		check = user.LoginPDB(username)
		if check == data:
			flash("Sorry, your data already saved")
			return redirect(url_for('visitors'))
		else: 
			user.insertDB(data)
			flash("You've successfully registration", "success")
			return redirect(url_for('formLogin'))
	return render_template('form.html')

@app.route('/login', methods=['POST', 'GET'])
def formLogin():
	if request.method == 'POST':
		username = request.form['namaUser']
		password = request.form['password']
		data = [username, password]
		user = User()
		psw = user.LoginPDB(username)
		if psw[0] is None:
			flash('Register firstly', 'warning')
			return redirect(url_for('visitors'))
		else:
			for acc in psw:
				if acc:
					session['username'] = username
					session['id'] = acc[0]
					return redirect(url_for('index'))
				else:
					flash('Password no detected by database', 'info')
					return redirect(url_for('visitors'))
	return render_template('login.html')

@login_required
@app.route('/update/<no>')
def search(no):
	book = EBook()
	data = book.getDBId(no)
	return render_template('Update.html', data=data)

@login_required
@app.route('/update', methods=['POST', 'GET'])
def update():
	book = EBook()
	iduser = session['id']
	data = book.getDBId(iduser)
	if request.method == 'POST':
		judul = request.form['judul']
		tahun = request.form['tahun']
		tipe = request.form['type']
		file = request.files['file']
		tup = (judul, tipe, tahun, secure_filename(file.filename), iduser)
		book = EBook()
		book.updateDB(tup)
		flash('Update Succes', 'success')
		return redirect(url_for('index'))
	return render_template('Update.html', data=data)

@login_required
@app.route('/search', methods=['POST', 'GET'])
def searching():
	book = EBook()
	search = request.form['search']
	data = book.searchDB(search)
	return redirect(url_for('public'))

@login_required
@app.route('/community', methods=['POST', 'GET'])
def community():
	komunitas = Komunitas()
	jumAll = komunitas.selectAll()
	iduser = session['id']
	if request.method == 'POST':
		namaKomunitas = request.form['namaKomunitas']
		namaUrl = request.form['urlKomunitas']
		data = (namaKomunitas, namaUrl)
		komunitas = Komunitas()
		komunitas.insertKom(data)
		flash("Your Community's added", "success")
		return render_template('Komunitas.html', all=jumAll,iduser=iduser)
	return render_template('Komunitas.html', all=jumAll,iduser=iduser)

@login_required
@app.route('/joinCom', methods=['POST', 'GET'])
def joinCommunity():
	iduser = session['id']
	komunitas = Komunitas()
	jumAll = komunitas.selectAll()
	if request.method == 'POST':
		namaKomunitas = request.form['namaKomunitas']
		data2 = (namaKomunitas, iduser)
		komunitas.joinKom(data2)
		flash("You've successfully join", "success")
		return render_template('Komunitas.html', all=jumAll, iduser=iduser)
	return render_template('Komunitas.html', all=jumAll,iduser=iduser)

import os
import json
from datetime import timedelta
from flask import Flask, request, jsonify, send_from_directory, render_template


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/download/<file>')
def download(file):
	if (file == 'test_plan'):
		alias = '思否博客测试计划.docx'
	elif (file == 'test_examples'):
		alias = '思否博客测试用例.xlsx'
	elif (file == 'test_report'):
		alias = '思否博客测试报告.docx'
	elif (file == 'test_demand'):
		alias = '思否博客需求文档.docx'
	elif (file == 'auto_scripts'):
		alias = 'scripts.rar'
	else:
		alias = file
	return send_from_directory(filename=alias, directory='./', as_attachment=True)


@app.route('/result')
def result():
	return render_template('res.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port='9998')

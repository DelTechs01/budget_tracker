from flask import Flask, render_template,request, redirect,url_for
from database import initiliaze_database,add_transaction, fetch_all_transactions
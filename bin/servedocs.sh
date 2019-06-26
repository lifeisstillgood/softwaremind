#firefox http://172.17.0.2:8000/_build/latex/TheDevManual.pdf
firefox http://172.17.0.2:8000/marketingsite/index.html &

cd /tmp
python -m http.server 8000

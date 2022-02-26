{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [26/Feb/2022 14:20:51] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2000 25 2000\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [26/Feb/2022 14:21:03] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "import joblib\n",
    "from flask import request, render_template\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        income = request.form.get(\"income\")\n",
    "        age = request.form.get(\"age\")\n",
    "        loan = request.form.get(\"loan\")\n",
    "        print(income, age, loan)\n",
    "        model=joblib.load(\"CreditDefault\")\n",
    "    #normalising the inputs\n",
    "        pred=model.predict([[((float(income)-45136.87597485758)/14423.382398409489),\n",
    "                             ((float(age)-34.795949606582)/12.838181998141051),\n",
    "                             ((float(loan)-5591.986694851936)/3174.059368326566)]])\n",
    "        print(pred)\n",
    "        s=\"The predicted default is: \" + str(pred[0])\n",
    "        return(render_template(\"index.html\", default = s))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", default = \"Predict Default\"))\n",
    "app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

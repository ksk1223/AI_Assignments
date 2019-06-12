{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 6.5  8.5 10.5 12.5]]\n",
      "[[-4.5 -4.5 -4.5 -4.5]]\n",
      "[[ 5.5 13.  22.5 34. ]]\n",
      "[[0.18181818 0.30769231 0.4        0.47058824]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = np.array([1,2,3,4])\n",
    "y = np.array([5.5,6.5,7.5,8.5])\n",
    "add=np.array([x+y])\n",
    "print(add)\n",
    "sub=np.array([x-y])\n",
    "print(sub)\n",
    "mult=np.array([x*y])\n",
    "print(mult)\n",
    "div=np.array([x/y])\n",
    "print(div)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [3 4]]\n",
      "[1 2]\n",
      "[3 4]\n",
      "[[1.         1.41421356]\n",
      " [1.73205081 2.        ]]\n",
      "[1.5 3.5]\n",
      "[1.5 3.5]\n",
      "[0.5 0.5]\n",
      "[[ 2.71828183  7.3890561 ]\n",
      " [20.08553692 54.59815003]]\n"
     ]
    }
   ],
   "source": [
    "#clm-0   row-1\n",
    "import numpy as np\n",
    "import math\n",
    "a=np.array([[1,2], [3,4]])\n",
    "print(a)\n",
    "print(np.min(a,axis=0))\n",
    "print(np.max(a,axis=0))\n",
    "print(np.sqrt(a))\n",
    "print(np.mean(a,axis=1))\n",
    "print(np.median(a,axis=1))\n",
    "print(np.std(a,axis=1))\n",
    "print(np.exp(a))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'q' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-133-8e2cc8bba323>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0msq\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mc\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mrem\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mq\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mbig\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mj\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[0mi\u001b[0m \u001b[1;33m<=\u001b[0m \u001b[0mn\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m    \u001b[1;32mwhile\u001b[0m \u001b[0mi\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m        \u001b[0mq\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mi\u001b[0m \u001b[1;33m/\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m        \u001b[0mrem\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mi\u001b[0m \u001b[1;33m%\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'q' is not defined"
     ]
    }
   ],
   "source": [
    " sq ,c,rem=0,q,big,i,j\n",
    "while i <= n:\n",
    "    while i > 0:\n",
    "        q = i / 10\n",
    "        rem = i % 10\n",
    "        c+1\n",
    "        count = c\n",
    "    sq = i * i\n",
    "    tempsq = sq\n",
    "    d = 1\n",
    "    while c > 0:\n",
    "        d = d * 10\n",
    "        c-1\n",
    "    j = 1\n",
    "    while j <= count:\n",
    "        q = sq / d\n",
    "        rm = sq % d\n",
    "        if i == rem:\n",
    "            big = tempsq\n",
    "            j+1\n",
    "    i+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def CountSquares(a, b): \n",
    "  \n",
    "    cnt = 0 # initialize result \n",
    "  \n",
    "    # Traverse through all numbers \n",
    "    for i in range (a, b + 1): \n",
    "        j = 1; \n",
    "        while j * j <= i: \n",
    "            if j * j == i: \n",
    "                 cnt = cnt + 1\n",
    "            j = j + 1\n",
    "        i = i + 1\n",
    "    return cnt \n",
    "CountSquares(1,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "ename": "UnboundLocalError",
     "evalue": "local variable 'i' referenced before assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnboundLocalError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-141-402cadb701d9>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     12\u001b[0m         \u001b[0mi\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mi\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mcnt\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 14\u001b[1;33m \u001b[0mCountSquares\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-141-402cadb701d9>\u001b[0m in \u001b[0;36mCountSquares\u001b[1;34m(a, b)\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[1;32mwhile\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m         \u001b[0mj\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m;\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m         \u001b[1;32mwhile\u001b[0m \u001b[0mj\u001b[0m \u001b[1;33m*\u001b[0m \u001b[0mj\u001b[0m \u001b[1;33m<=\u001b[0m \u001b[0mi\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mj\u001b[0m \u001b[1;33m*\u001b[0m \u001b[0mj\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0mi\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m                  \u001b[0mcnt\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcnt\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mUnboundLocalError\u001b[0m: local variable 'i' referenced before assignment"
     ]
    }
   ],
   "source": [
    "def CountSquares(a, b): \n",
    "  \n",
    "    cnt = 0 # initialize result \n",
    "  \n",
    "    \n",
    "    while range(a,b+1): \n",
    "        j = 1; \n",
    "        while j * j <= i: \n",
    "            if j * j == i: \n",
    "                 cnt = cnt + 1\n",
    "            j = j + 1\n",
    "        i = i + 1\n",
    "    return cnt \n",
    "CountSquares(1,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

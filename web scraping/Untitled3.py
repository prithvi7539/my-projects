{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyMc44xJLiDqb60rbJc51uyi"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":20,"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":366},"id":"wqyKn0D_L55e","executionInfo":{"status":"error","timestamp":1698127573007,"user_tz":-330,"elapsed":464,"user":{"displayName":"prithvi pvr","userId":"04025769005514087179"}},"outputId":"0109f449-f8ca-48a7-f4b1-0c861c20da9e"},"outputs":[{"output_type":"error","ename":"TclError","evalue":"ignored","traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mTclError\u001b[0m                                  Traceback (most recent call last)","\u001b[0;32m<ipython-input-20-9c86b0c0b8a0>\u001b[0m in \u001b[0;36m<cell line: 20>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m             \u001b[0mfile\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1.0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mEND\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0mroot\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTk\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m \u001b[0mroot\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Text Editor\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/usr/lib/python3.10/tkinter/__init__.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, screenName, baseName, className, useTk, sync, use)\u001b[0m\n\u001b[1;32m   2297\u001b[0m                 \u001b[0mbaseName\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbaseName\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mext\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2298\u001b[0m         \u001b[0minteractive\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2299\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtk\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_tkinter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcreate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mscreenName\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbaseName\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclassName\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minteractive\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwantobjects\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0museTk\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msync\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2300\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0museTk\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2301\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_loadtk\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;31mTclError\u001b[0m: no display name and no $DISPLAY environment variable"]}],"source":[]}]}
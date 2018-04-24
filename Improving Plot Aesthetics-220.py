## 3. Introduction To The Data ##

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
plt.plot(women_degrees["Year"],women_degrees["Biology"])
plt.show()

## 4. Visualizing The Gender Gap ##

import pandas as pd
import matplotlib.pyplot as plt
women_degrees =pd.read_csv("percent-bachelors-degrees-women-usa.csv")

plt.plot(women_degrees['Year'],women_degrees["Biology"],c='blue',label='Women')

plt.plot(women_degrees['Year'],100-(women_degrees["Biology"].values),c='green',label='Men')
plt.legend(loc="upper right")
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.show()




## 6. Hiding Tick Marks ##

import pandas as pd
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
women_degrees =pd.read_csv("percent-bachelors-degrees-women-usa.csv")

ax.plot(women_degrees['Year'],women_degrees["Biology"],c='blue',label='Women')

ax.plot(women_degrees['Year'],100-(women_degrees["Biology"].values),c='green',label='Men')

ax.tick_params(bottom="off",top="off",left="off",right="off")
ax.legend(loc="upper right")
ax.set_title("Percentage of Biology Degrees Awarded By Gender")

plt.show()


## 7. Hiding Spines ##

import pandas as pd
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
women_degrees =pd.read_csv("percent-bachelors-degrees-women-usa.csv")

ax.plot(women_degrees['Year'],women_degrees["Biology"],c='blue',label='Women')

ax.plot(women_degrees['Year'],100-(women_degrees["Biology"].values),c='green',label='Men')

ax.tick_params(bottom="off",top="off",left="off",right="off")
ax.legend(loc="upper right")

ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["top"].set_visible(False)


ax.set_title("Percentage of Biology Degrees Awarded By Gender")

plt.show()


## 8. Comparing Gender Gap Across Degree Categories ##

import pandas as pd
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(12,12))
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

women_degrees =pd.read_csv("percent-bachelors-degrees-women-usa.csv")

ax1.plot(women_degrees['Year'],women_degrees["Biology"],c='blue',label='Women')
ax1.plot(women_degrees['Year'],100-women_degrees["Biology"].values,c='green',label='Men')


ax1.tick_params(bottom="off",top="off",left="off",right="off")
ax1.legend(loc="upper right")
ax1.spines["right"].set_visible(False)
ax1.spines["left"].set_visible(False)
ax1.spines["bottom"].set_visible(False)
ax1.spines["top"].set_visible(False)
ax1.set_title("Biology")

ax1.plot(women_degrees['Year'],100-women_degrees["Biology"].values,c='green',label='Men')


ax2.plot(women_degrees['Year'],100-(women_degrees["Computer Science"].values),c='green',label='Men')
ax2.plot(women_degrees['Year'],women_degrees["Computer Science"],c='blue',label='Women')
ax2.tick_params(bottom="off",top="off",left="off",right="off")
ax2.legend(loc="upper right")
ax2.spines["right"].set_visible(False)
ax2.spines["left"].set_visible(False)
ax2.spines["bottom"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax2.set_title("Computer Science")


ax3.plot(women_degrees['Year'],100-(women_degrees["Engineering"].values),c='green',label='Men')
ax3.plot(women_degrees['Year'],women_degrees["Engineering"],c='blue',label='Women')
ax3.tick_params(bottom="off",top="off",left="off",right="off")
ax3.legend(loc="upper right")
ax3.spines["right"].set_visible(False)
ax3.spines["left"].set_visible(False)
ax3.spines["bottom"].set_visible(False)
ax3.spines["top"].set_visible(False)
ax3.set_title("Engineering")



ax4.plot(women_degrees['Year'],100-(women_degrees["Math and Statistics"].values),c='green',label='Men')
ax4.plot(women_degrees['Year'],women_degrees["Math and Statistics"],c='blue',label='Women')
ax4.tick_params(bottom="off",top="off",left="off",right="off")
ax4.legend(loc="upper right")
ax4.spines["right"].set_visible(False)
ax4.spines["left"].set_visible(False)
ax4.spines["bottom"].set_visible(False)
ax4.spines["top"].set_visible(False)
ax4.set_title("Math and Statistics")



plt.show()
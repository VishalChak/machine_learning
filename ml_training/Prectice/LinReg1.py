from sklearn import linear_model
import matplotlib.pyplot as ply

x = [[6],[8],[10],[14],[18]]
y = [[7],[9],[13],[17.5],[18]]

ply.figure()

ply.title("pIzz price")
ply.ylabel("YY")
ply.xlabel("XX")
ply.grid(True)
ply.plot(x,y,'k.')
ply.show()

model = linear_model.LinearRegression()
model.fit(x,y)

x_test = [[8],[9],[11],[16],[12]]
y_test = [[11],[8.5],[15],[18],[11]]

score = model.score(x_test,y_test)

print("R-Squred: {0},, coffi{1}".format(score, model.coef_))


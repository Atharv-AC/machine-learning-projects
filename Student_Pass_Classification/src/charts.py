import matplotlib.pyplot as plt
import os


base_path = os.path.dirname(__file__)

reports_dir = os.path.join(base_path, "..", "reports")

# Create folder if it doesn't exist
os.makedirs(reports_dir, exist_ok=True)

# paths where the charts are saved
passfail = os.path.join(reports_dir, "Pass_Fail_chart.svg")
Scatter_save = os.path.join(reports_dir, "Scatter_chart.svg")
Histo_save = os.path.join(reports_dir, "Probability.svg")
curve_save = os.path.join(reports_dir, "ROC_curve.svg")
dist_save = os.path.join(reports_dir, "Math_distribution.svg")





def pass_fail_chart(df):
    plt.figure(facecolor="#f9dfe6")
    df["pass"].value_counts().plot(kind="bar", color=["#6C1868", "#C10C97"])
    plt.title("Pass vs Fail Distribution")
    plt.ylabel("Count")
    plt.gca().set_facecolor("#fed3e0") 
    plt.savefig(passfail)
    plt.show()
    plt.close()


def score_distribution(df):
    plt.figure(facecolor="#f4ffb8")
    df["math_score"].hist(color="#E69A72", edgecolor="black")
    plt.title("Math Score Distribution")
    plt.gca().set_facecolor("#ffffc0") 
    plt.savefig(dist_save)
    plt.show()
    plt.close()


def scatter_chart(df):
    plt.figure(facecolor="#effde4")
    plt.scatter(df["math_score"], df["writing_score"], color="#0e7468")
    plt.xlabel("Math Score")
    plt.ylabel("Writing Score")
    plt.title("Math vs Writing Relationship")
    plt.gca().set_facecolor("#e2fade") 
    plt.savefig(Scatter_save)
    plt.show()
    plt.close()


def histo(model, X_test):
    plt.figure(facecolor="#f7efd1")
    probs = model.predict_proba(X_test)[:,1]

    plt.hist(probs, bins=20, color="#db6d23", edgecolor="black")
    plt.title("Prediction Probability Distribution")
    plt.gca().set_facecolor("#f9f2d9") 
    plt.savefig(Histo_save)
    plt.show()
    plt.close()



def curve(model, X_test, y_test):
    plt.figure(facecolor="#eafdff")
    from sklearn.metrics import roc_curve, auc
    probs = model.predict_proba(X_test)[:,1]
    fpr, tpr, _ = roc_curve(y_test, probs)

    plt.plot(fpr, tpr)
    plt.plot([0,1],[0,1])
    plt.title("ROC Curve")
    plt.gca().set_facecolor("#effdfb") 
    plt.savefig(curve_save)
    plt.show()
    plt.close()

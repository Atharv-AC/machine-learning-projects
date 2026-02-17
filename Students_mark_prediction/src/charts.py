import matplotlib.pyplot as plt 
import os 


base_path = os.path.dirname(__file__)
# paths where the charts are saved
corelation_M_R = os.path.join(base_path, "..", "reports", "MathRead_corelation.svg")
corelation_W_R = os.path.join(base_path, "..", "reports", "writeRead_corelation.svg")
ActualPred_save = os.path.join(base_path, "..", "reports", "ActualPred_corelation.svg")
Residual_save = os.path.join(base_path, "..", "reports", "ResidualChart.svg")
dist_save = os.path.join(base_path, "..", "reports", "HistrogramChart.svg")




def corelationMathRead(df):
    # 1. Plotting the data to see if there is any correlation between the math score and reading score.
    # plt.scatter(df['math_score'], df['reading_score'], color=["#4CAF50", "#2196F3", "#FF9800"])
    plt.figure(facecolor="#f9b1c2")
    plt.scatter(df['math_score'], df['reading_score'], color=["#800404" ])
    plt.xlabel('Math Score')
    plt.ylabel('Reading Score')
    plt.title('Math Score vs Reading Score')
    plt.gca().set_facecolor("#fcc1ca")   # light gray background
    plt.savefig(corelation_M_R, facecolor=plt.gcf().get_facecolor(), dpi=400, bbox_inches="tight")
    plt.show()
    plt.close()


def corelationWriteRead(df):
    # 2. Plotting the data to see if there is any correlation between the writing score and reading score.
    plt.figure(facecolor="#e5f9a5")
    plt.scatter(df['writing_score'], df['reading_score'], color="#2BB836")
    plt.xlabel('Writing Score')
    plt.ylabel('Reading Score')
    plt.title('Writing Score vs Reading Score')
    plt.gca().set_facecolor("#e0fcb5")   # light gray background
    plt.savefig(corelation_W_R, facecolor=plt.gcf().get_facecolor(),bbox_inches="tight")
    plt.show()
    plt.close()


def ActualPred_chart(y_test, pred):
    # y_test is the actual reading score and pred is the predicted reading score.
    plt.figure(facecolor="#fde2d2")
    plt.scatter(y_test, pred,  color="#B7573A")
    plt.xlabel("Actual Reading Score")
    plt.ylabel("Predicted Reading Score")
    plt.title('Actual Score vs Predicted Score')
    plt.gca().set_facecolor("#fdd3c5")   # light gray background
    plt.savefig(ActualPred_save, facecolor=plt.gcf().get_facecolor(), dpi=400, bbox_inches="tight")
    plt.show()
    plt.close()

# Residuals are the differences between the actual values and the predicted values.
# Residuals = Actual - Predicted
def residuals_chart(y_test, pred):
    residuals = y_test - pred
    plt.figure(facecolor="#edd2f7")
    plt.scatter(pred, residuals, color="#673AB7")
    plt.axhline(0)
    plt.xlabel("Predicted Reading Score")
    plt.ylabel("Residuals")
    plt.title('Residual Chart')
    plt.gca().set_facecolor("#f7e3fa")   # light gray background
    plt.savefig(Residual_save, facecolor=plt.gcf().get_facecolor(), dpi=400, bbox_inches="tight")
    plt.show()
    plt.close()


def distribution_chart(y_test, pred):
    plt.figure(facecolor="#efffca")
    residuals = y_test - pred
    plt.hist(residuals, bins=20, color="#FF9800", edgecolor="black")
    plt.title("Score Distribution")
    plt.xlabel("Actual Score")
    plt.ylabel("Predicted")
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.gca().set_facecolor("#f4f9c5")   # light gray background
    plt.savefig(dist_save, facecolor=plt.gcf().get_facecolor(), dpi=400, bbox_inches="tight")
    plt.show()
    plt.close()
    # print(y_test)
    # print(pred)
    # print(residuals)

    
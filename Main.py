
import Load as LD
import CumSum as CS
# Excel File
ef = 'Uniform Sections & Back-calcs_N7-7 0-65 ct 231116.xlsx'
RL = LD.Load(ef)

print("Start[km]\tEnd[km]\tLeft Rutting\tRight Rutting \t CumRight \t CumLeft")
# Get lists from the Load instance
left_list = RL.get_left_list()
right_list = RL.get_right_list()
CSR=CS.CumSum(right_list)
CSL=CS.CumSum(left_list)
# Iterate and print
for i in range(len(left_list)):
    print(left_list[i], "\t\t\t  ",   right_list[i],"\t\t\t  ",CSR.get_cumsum()[i],"\t\t\t  ",CSL.get_cumsum()[i])

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:56:10 2023

@author: tan78
"""
import numpy as np
import pandas as pd

class NeuralNetwork:
        
    def __init__(self, input_size, output_size, weight_input, weight_output):
        self.input_size = input_size
        self.output_size = output_size
        self.weight_input = weight_input
        self.weight_output = weight_output
        self.name_type = ""
    
    
    #Phương thức set và get
    def setInput_size(self, input_size):
        self.input_size = input_size
        
    def getInput_size(self):
        return self.input_size
    
    def setOutput_size(self, output_size):
        self.output_size = output_size
        
    def getOutput_size(self):
        return self.output_size
    
    def setWeight_input(self, weight_input):
        self.weight_input = weight_input
        
    def getWeight_input(self):
        return self.weight_input
    
    def setWeight_output(self, weight_output):
        self.weight_output = weight_output
    
    def getWeight_output(self):
        return self.weight_output
    
    def getName_request(self):
        return self.name_request
    
    def setName_type(self):
        names_type =[]
        name_type = ""
        for request_out in self.output_size:
            if(request_out[0] ==1):
                name_type += "to"
            else:
                name_type += "nhỏ"
            
            if(request_out[1] ==1):
                name_type += " chín"
            else:
                name_type += " xanh"
            
            if(request_out[2] ==1):
                name_type += " tươi"
            else:
                name_type += " héo"
            names_type.append(name_type)
            name_type = ""
        self.name_type = np.array(names_type)
        
    def hardLim(self):
        kiemtra = True
        n = 0
        for input_ in self.input_size:
            hardlim = self.weight_input.dot(input_)+ self.weight_output
            i = 0
            for j in hardlim:
                if (hardlim[i] < 0):
                    hardlim[i] = 0
                else:
                    hardlim[i] = 1
                i = i + 1
            
            if(np.array_equal(hardlim, neuralNetwork.output_size[n]) == False):
                kiemtra = False
                self.weight_input += (self.output_size[n] - hardlim).dot(input_.transpose())
                self.weight_output += (self.output_size[n] - hardlim)
            n = n + 1
        return kiemtra
    
    def train(self):
        l = 1
        while(True):
            if(neuralNetwork.hardLim() == True):
                break
            print("Vòng : ", l)
            print(neuralNetwork.getWeight_input())
            print(neuralNetwork.getWeight_output())
            l = l + 1
    
    def request(self):
        request_output = []
        for request in self.input_size:
            hardlim = self.weight_input.dot(request)+ self.weight_output
            i = 0
            for j in hardlim:
                if (hardlim[i] < 0):
                    hardlim[i] = 0
                else:
                    hardlim[i] = 1
                i = i + 1
            request_output.append(hardlim)
            
        self.output_size = np.array(request_output)
    
    def display(self):
        # tạo dict từ các series
        s = {}
        cot_can_nang = []
        cot_do_chin = []
        cot_do_tuoi = []
        cot_loai = []
        cot_to_nho = []
        cot_xanh_chin = []
        cot_heo_tuoi = []
        cot_stt = []
        index = []
        i = 1
        for input_dv in self.input_size:
            cot_stt.append(i)
            i = i+1
            cot_can_nang.append(int(input_dv[0]))
            cot_do_chin.append(int(input_dv[1]))
            cot_do_tuoi.append(int(input_dv[2]))
        
        for input_loai in self.name_type:
            cot_loai.append(input_loai)
        
        for output_request in self.getOutput_size():
            cot_to_nho.append(int(output_request[0]))
            cot_xanh_chin.append(int(output_request[1]))
            cot_heo_tuoi.append(int(output_request[2]))
            
        nhan = ["STT","Cân nặng", "Độ chín", "Độ tuổi", "Loại", "To/nhỏ", "Xanh/chín", "Héo/tươi"]
        s = {'STT': pd.Series(cot_stt),
         'Cân nặng': pd.Series(cot_can_nang),
         'Độ chín': pd.Series(cot_do_chin),
         'Độ tuổi': pd.Series(cot_do_tuoi),
         'Loại': pd.Series(cot_loai),
         'To/nhỏ': pd.Series(cot_to_nho),
         'Xanh/chín': pd.Series(cot_xanh_chin),
         'Héo/tươi': pd.Series(cot_heo_tuoi)
         
         }

        # tại DataFrame từ dict
        df = pd.DataFrame(s)

        print(df)
    
    def export_to_excel(self, filename):
        # tạo dict từ các series
        s = {}
        cot_can_nang = []
        cot_do_chin = []
        cot_do_tuoi = []
        cot_loai = []
        cot_to_nho = []
        cot_xanh_chin = []
        cot_heo_tuoi = []
        cot_stt = []
        index = []
        i = 1
        for input_dv in self.input_size:
            cot_stt.append(i)
            i = i+1
            cot_can_nang.append(int(input_dv[0]))
            cot_do_chin.append(int(input_dv[1]))
            cot_do_tuoi.append(int(input_dv[2]))
        
        for input_loai in self.name_type:
            cot_loai.append(input_loai)
        
        for output_request in self.getOutput_size():
            cot_to_nho.append(int(output_request[0]))
            cot_xanh_chin.append(int(output_request[1]))
            cot_heo_tuoi.append(int(output_request[2]))
            
        nhan = ["STT","Cân nặng", "Độ chín", "Độ tuổi", "Loại", "To/nhỏ", "Xanh/chín", "Héo/tươi"]
        s = {'STT': pd.Series(cot_stt),
         'Cân nặng': pd.Series(cot_can_nang),
         'Độ chín': pd.Series(cot_do_chin),
         'Độ tuổi': pd.Series(cot_do_tuoi),
         'Loại': pd.Series(cot_loai),
         'To/nhỏ': pd.Series(cot_to_nho),
         'Xanh/chín': pd.Series(cot_xanh_chin),
         'Héo/tươi': pd.Series(cot_heo_tuoi)
         
         }

        # tại DataFrame từ dict
        df = pd.DataFrame(s)

        print(df)
        # Tạo dataframe từ dữ liệu inputs và targets
        # Xuất DataFrame ra file Excel
        df.to_excel(filename, index=False)
        
def get_data_onExel(namefile):
    train_inputs = []
    train_targets = []
    
    train_input = []
    train_target = []    
    
    Df = pd.DataFrame(pd.read_excel(namefile))
    canNang = Df.loc[:,'Cân nặng']
    doChin = Df.loc[:,'Độ chín']
    doTuoi = Df.loc[:,'Độ tuổi']
    toNho = Df.loc[:,'To/nhỏ']
    xanhChin = Df.loc[:,'Xanh/chín']
    heoTuoi = Df.loc[:,'Héo/tươi']
    i = 0
    for o_can_nang in doChin:
     
        canNan = [canNang[i]]
        train_input.append(canNan)
        doChi = [doChin[i]]
        train_input.append(doChi)
        doTuo = [doTuoi[i]]
        train_input.append(doTuo)
        toNh = [toNho[i]]
        train_target.append(toNh)
        xanhChi = [xanhChin[i]]
        train_target.append(xanhChi)
        heoTuo = [heoTuoi[i]]
        train_target.append(heoTuo)
        
        train_inputs.append(train_input)
        train_targets.append(train_target)
        
        train_input = []
        train_target = []
        i = i + 1
    return train_inputs,train_targets
def get_input_data(namefile):
    train_inputs = []
    train_targets = []
    
    train_input = []
    train_target = []

    print("Nhập 1: lấy dữ liệu huấn luyện từ file train.")
    print("Nhập 2: nhập dữ liệu từ bàn phím")
    print("Nhập 3: lấy dữ liệu của Hải Anh")
    luaChon = int(input("Lựa chọn := "))
    if(luaChon==1):
        train_inputs, train_targets = get_data_onExel(namefile)
    elif (luaChon ==3):
        # Tạo dữ liệu huấn luyện từ bàn phím
        train_inputs = [[[1],[1],[4]],  [[2],[2],[6]],  [[8],[1],[6]],  [[9],[3],[8]],  [[2],[7],[7]],  [[3],[8],[5]],  [[8],[8],[6]],  [[9],[9],[4]]]
        train_targets = [[[0], [0], [0]],    [[0], [0], [1]],     [[1], [0], [1]],    [[1], [0], [1]],      [[0], [1], [1]],     [[0], [1], [0]],     [[1], [1], [1]],     [[1], [1], [0]]]
    else:
        # Nhập số lượng mẫu và số thuộc tính từ bàn phím
        num_samples = int(input("Nhập số lượng mẫu huấn luyện: "))
        for i in range(0,num_samples):
            train_input = []
            train_target = []
            thuoctinh1 = int(input("Thuộc tính 1: "))
            thuoctinh1 = [thuoctinh1]
            thuoctinh2 = int(input("Thuộc tính 2: "))
            thuoctinh2 = [thuoctinh2]
            thuoctinh3 = int(input("Thuộc tính 3: "))
            thuoctinh3 = [thuoctinh3]
            
            daura1 = int(input("Đầu ra 1: "))
            daura1 = [daura1]
            daura2 = int(input("Đầu ra 2: "))
            daura2 = [daura2]
            daura3 = int(input("Đầu ra 3: "))
            daura3 = [daura3]
            
            train_input.append(thuoctinh1)
            train_input.append(thuoctinh2)
            train_input.append(thuoctinh3)
            train_inputs.append(train_input)
            
            train_target.append(daura1)
            train_target.append(daura2)
            train_target.append(daura3)
            train_targets.append(train_target)
            
    return np.array(train_inputs), np.array(train_targets)

def get_weight():
    
    #num_weight_input =  [[11, -6, -7],    [-1, 15, -3],     [ 1, -9, 34]]
    num_weight_input =  [[11, -6, -7],      [-1, 15, -3],   [ 0, -5, 43]]
    
    #num_weight_output = [[  19],[ -21],[-136]]
    num_weight_output = [[  19],    [ -21],     [-133]]
    return np.array(num_weight_input), np.array(num_weight_output)

def get_request_data(filename):
    request_input = []
    
    print("Nhập 1. Lấy dữ liệu cần kiểm tra từ file exel")
    print("Nhập 2. Lấy dữ liệu cần kiểm tra từ bàn phím")
    luaChon = int(input("Lựa chọn := "))
    if(luaChon == 1):
        request_input, request_output = get_data_onExel(filename)
    else:
        # Nhập số lượng mẫu cần kiểm tra
        num_request = int(input("Nhập số lượng mẫu cần kiểm tra: "))
        
        
        # Tạo dữ liệu cần kiểm tra
        for i in range(0,num_request):
            request = []
            print("Mẫu ",i+1)
            thuoctinh1 = int(input("Thuộc tính 1: "))
            thuoctinh1 = [thuoctinh1]
            thuoctinh2 = int(input("Thuộc tính 2: "))
            thuoctinh2 = [thuoctinh2]
            thuoctinh3 = int(input("Thuộc tính 3: "))
            thuoctinh3 = [thuoctinh3]
            request.append(thuoctinh1)
            request.append(thuoctinh2)
            request.append(thuoctinh3)
            request_input.append(request)
    return np.array(request_input)

if __name__ == "__main__":
    num_weight_input,num_weight_output = get_weight()
    num_input_size, num_output_size = get_input_data("huanluyen.xlsx") 
    
    neuralNetwork = NeuralNetwork(num_input_size, num_output_size, num_weight_input, num_weight_output)
    neuralNetwork.setName_type()
    neuralNetwork.train()
    
    
    request_input = get_request_data("kiemtra.xlsx")
    neuralNetwork2 = NeuralNetwork(request_input,[],neuralNetwork.weight_input, neuralNetwork.weight_output)
    neuralNetwork2.request()
    neuralNetwork2.setName_type()
    
    print("Dữ liệu huấn luyện")
    neuralNetwork.display()
    
    print("Dữ liệu kiểm tra")
    neuralNetwork2.display()
    print("Bạn muốn xuất ra file exel không")
    print("Nhấn 1 là có")
    print("Nhấn 2 là không")
    luachon = int(input("Lựa chọn := "))
    if(luachon==1):
        namefile1 = ""
        namefile2 = ""
        
        print("Nhập tên file để xuất dữ liệu huấn luyện")
        namefile1 = input("Tên file := ")
        namefile1 = namefile1 + ".xlsx"        
        neuralNetwork.export_to_excel(namefile1)
        
        print("Nhập tên file để xuất dữ liệu cần kiểm tra")
        namefile2 = input("Tên file := ")
        namefile2 = namefile2 + ".xlsx" 
        neuralNetwork2.export_to_excel(namefile2)
    
        
    
   
        
        
    
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
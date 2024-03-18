from format_data import *
from copy import deepcopy

def print_DataFile(s: DataFile):
    print("basic ifo:", s.basic_ifo.id, s.basic_ifo.observe_time, s.basic_ifo.latitude, s.basic_ifo.longitude, 
          s.basic_ifo.altitude, s.basic_ifo.QC_flag)
    print("TH:", s.TH.temperature, s.TH.high_temp, s.TH.high_temp_time, s.TH.low_temp, s.TH.low_temp_time, 
          s.TH.dew_temp, s.TH.hum, s.TH.low_hum, s.TH.low_hum_time, s.TH.pressure)
    print("RE:", s.RE.rain_sum)
    print("WI:", s.WI.wind_dir2, s.WI.avg_speed2, s.WI.wind_dir10, s.WI.avg_speed10, s.WI.high_wind_dir,
          s.WI.high_wind_speed, s.WI.high_speed_time, s.WI.rsc_dir, s.WI.rsc_speed, s.WI.max_dir, s.WI.max_speed,
          s.WI.max_speed_time, s.WI.max_dir_minute, s.WI.max_speed_minute, s.WI.max_speed_time_minute)
    print("RT:", s.RT.road_temp, s.RT.road_high_temp, s.RT.road_high_temp_time, s.RT.road_low_temp, s.RT.road_low_temp_time,
          s.RT.base_temp)
    print("VV:", s.VV.avg_vis_minute, s.VV.low_vis, s.VV.low_vis_time)
    print("RS:", s.RS.road_state, s.RS.snow_thick, s.RS.water_thick, s.RS.ice_thick, s.RS.ice_temp, s.RS.deicer_con)
    print("WW:", s.WW.weather_code)
    print("MR:", s.MR.rain_hour_minute)
    print("QC:")
    print("Q1:", s.QC.Q1)
    print("Q2:", s.QC.Q2)
    print("Q3:", s.QC.Q3)


def print_StateFile(s: StateFile):
    print("basic ifo:", s.basic_ifo.id, s.basic_ifo.observe_time, s.basic_ifo.latitude, s.basic_ifo.longitude, 
          s.basic_ifo.altitude, s.basic_ifo.QC_flag)
    print("ST:", s.ST.main_state, s.ST.main_volt, s.ST.main_power_type, s.ST.main_cpu_temp, s.ST.main_AD, s.ST.main_timer,
          s.ST.main_SSD, s.ST.main_GPS, s.ST.main_door, s.ST.human_near, s.ST.solar_pad, s.ST.temp_sr, s.ST.hum_sr,
          s.ST.wind_dir_sr, s.ST.wind_speed_sr, s.ST.rain_sr, s.ST.road_temp_sr, s.ST.base_temp_sr, s.ST.road_state_sr, s.ST.vis_sr)

def read_data(line_data: list, index: int):
    cur_data = DataFile(index)
    basic = line_data[0].split()
    m1 = len(basic)
    
    try:
        assert(m1 == 6)      #读取基本信息段
        
        assert(len(basic[0]) == 5)
        cur_data.basic_ifo.id = basic[0]
        assert(len(basic[1]) == 14)
        cur_data.basic_ifo.observe_time = basic[1]
        assert(len(basic[2]) == 6)
        cur_data.basic_ifo.latitude = basic[2]
        assert(len(basic[3]) == 7)
        cur_data.basic_ifo.longitude = basic[3]
        assert(len(basic[4]) == 5)
        cur_data.basic_ifo.altitude = basic[4]
        assert(len(basic[5]) == 3)
        cur_data.basic_ifo.QC_flag = basic[5]
    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile()
    
    cur_TH = line_data[1].split()
    m2 = len(cur_TH)
    
    try:
        assert(m2 == 10 + 1)      #读取温湿度
        
        assert(len(cur_TH[1]) == 4)
        cur_data.TH.temperature = cur_TH[1]
        assert(len(cur_TH[2]) == 4)
        cur_data.TH.high_temp = cur_TH[2]
        assert(len(cur_TH[3]) == 4)
        cur_data.TH.high_temp_time = cur_TH[3]
        assert(len(cur_TH[4]) == 4)
        cur_data.TH.low_temp = cur_TH[4]
        assert(len(cur_TH[5]) == 4)
        cur_data.TH.low_temp_time = cur_TH[5]
        assert(len(cur_TH[6]) == 4)
        cur_data.TH.dew_temp = cur_TH[6]
        assert(len(cur_TH[7]) == 3)
        cur_data.TH.hum = cur_TH[7]
        assert(len(cur_TH[8]) == 3)
        cur_data.TH.low_hum = cur_TH[8]
        assert(len(cur_TH[9]) == 4)
        cur_data.TH.low_hum_time = cur_TH[9]
        assert(len(cur_TH[10]) == 3)
        cur_data.TH.pressure = cur_TH[10]
    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile()
    
    cur_RE = line_data[2].split()
    m3 = len(cur_RE)
    try:
        assert(m3 == 2)     #读取累计降水量

        assert(len(cur_RE[1]) == 4)
        cur_data.RE.rain_sum = cur_RE[1]
    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile()
    
    cur_WI = line_data[3].split()
    m4 = len(cur_WI)
    try:
        assert(m4 == 15)
        
        #此时的观测时间,WI字段里要加上
        cur_data.WI.max_speed_time_minute = cur_data.basic_ifo.observe_time[8: 12]
        assert(len(cur_WI[1]) == 3)
        cur_data.WI.wind_dir2 = cur_WI[1]
        assert(len(cur_WI[2]) == 3)
        cur_data.WI.avg_speed2 = cur_WI[2]
        assert(len(cur_WI[3]) == 3)
        cur_data.WI.wind_dir10 = cur_WI[3]
        assert(len(cur_WI[4]) == 3)
        cur_data.WI.avg_speed10 = cur_WI[4]
        assert(len(cur_WI[5]) == 3)
        cur_data.WI.high_wind_dir = cur_WI[5]
        assert(len(cur_WI[6]) == 3)
        cur_data.WI.high_wind_speed = cur_WI[6]
        assert(len(cur_WI[7]) == 4)
        cur_data.WI.high_speed_time = cur_WI[7]
        assert(len(cur_WI[8]) == 3)
        cur_data.WI.rsc_dir = cur_WI[8]
        assert(len(cur_WI[9]) == 3)
        cur_data.WI.rsc_speed = cur_WI[9]
        assert(len(cur_WI[10]) == 3)
        cur_data.WI.max_dir = cur_WI[10]
        assert(len(cur_WI[11]) == 3)
        cur_data.WI.max_speed = cur_WI[11]
        assert(len(cur_WI[12]) == 4)
        cur_data.WI.max_speed_time = cur_WI[12]
        assert(len(cur_WI[13]) == 3)
        cur_data.WI.max_dir_minute = cur_WI[13]
        assert(len(cur_WI[14]) == 3)
        cur_data.WI.max_speed_minute = cur_WI[14]
    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile() 

    cur_RT = line_data[4].split()
    m5 = len(cur_RT)
    try:
        assert(m5 == 6 + 1)
        for i in range(1, 7):
            assert(len(cur_RT[i]) == 4)
        cur_data.RT.road_temp = cur_RT[1]
        cur_data.RT.road_high_temp = cur_RT[2]
        cur_data.RT.road_high_temp_time = cur_RT[3]
        cur_data.RT.road_low_temp = cur_RT[4]
        cur_data.RT.road_low_temp_time = cur_RT[5]
        cur_data.RT.base_temp = cur_RT[6]

    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile() 

    cur_VV = line_data[5].split()
    m6 = len(cur_VV)
    try:
        assert(m6 == 3 + 1)
        assert(len(cur_VV[1]) == 5)
        cur_data.VV.avg_vis_minute = cur_VV[1]
        assert(len(cur_VV[2]) == 5)
        cur_data.VV.low_vis = cur_VV[2]
        assert(len(cur_VV[3]) == 4)
        cur_data.VV.low_vis_time = cur_VV[3]

    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile() 

    cur_RS = line_data[6].split()
    m7 = len(cur_RS)
    try:
        assert(m7 == 6 + 1)
        assert(len(cur_RS[1]) == 2 + 4)
        cur_data.RS.road_state = cur_RS[1][0: 2]    #把后边的'----'去掉
        assert(len(cur_RS[2]) == 4)
        cur_data.RS.snow_thick = cur_RS[2]
        assert(len(cur_RS[3]) == 4)
        cur_data.RS.water_thick = cur_RS[3]
        assert(len(cur_RS[4]) == 4)
        cur_data.RS.ice_thick = cur_RS[4]
        assert(len(cur_RS[5]) == 4)
        cur_data.RS.ice_temp = cur_RS[5]
        assert(len(cur_RS[6]) == 3)
        cur_data.RS.deicer_con = cur_RS[6]


    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile() 
    
    cur_WW = line_data[7].split()
    m8 = len(cur_WW)
    try:
        assert(m8 == 1 + 1)
        assert(len(cur_WW[1]) == 12)
        cur_data.WW.weather_code = cur_WW[1]
    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile() 
    
    cur_MR = line_data[8].split()
    m9 = len(cur_MR)
    try:
        assert(m9 == 1 + 1)
        assert(len(cur_MR[1]) == 120)
        cur_data.MR.rain_hour_minute = cur_MR[1]
    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile() 
    
    try:    #读取最后的QC码和EOF
        cur_data.QC.Q1 = line_data[10][3:]
        cur_data.QC.Q2 = line_data[11][3:]
        cur_data.QC.Q3 = line_data[12][3: len(line_data[12]) - 1] #最后多了个“=”号，去掉
        
        cur_data.EOF = line_data[13].split()
    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile() 
    return True, cur_data




def read_state(line_data: list, index: int):
    cur_data = StateFile(index)
    basic = line_data[0].split()
    m1 = len(basic)
    
    try:
        assert(m1 == 6)      #读取基本信息段
        
        assert(len(basic[0]) == 5)
        cur_data.basic_ifo.id = basic[0]
        assert(len(basic[1]) == 14)
        cur_data.basic_ifo.observe_time = basic[1]
        assert(len(basic[2]) == 6)
        cur_data.basic_ifo.latitude = basic[2]
        assert(len(basic[3]) == 7)
        cur_data.basic_ifo.longitude = basic[3]
        assert(len(basic[4]) == 5)
        cur_data.basic_ifo.altitude = basic[4]
        assert(len(basic[5]) == 3)
        cur_data.basic_ifo.QC_flag = basic[5]
    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile()
    
    state = line_data[1].split()
    #ST字段12序号那里有错位，自己修正了
    #最后一个能见度直接把最后两段并起来了
    m2 = len(state)
    try:
        assert(m2 == 21 + 2)
        assert(len(state[1]) == 1)
        cur_data.ST.main_state = state[1]
        assert(len(state[2]) == 4)
        cur_data.ST.main_volt = state[2]
        assert(len(state[3]) == 1)
        cur_data.ST.main_power_type = state[3]
        assert(len(state[4]) == 4)
        cur_data.ST.main_cpu_temp = state[4]
        assert(len(state[5]) == 1)
        cur_data.ST.main_AD = state[5]
        assert(len(state[6]) == 1)
        cur_data.ST.main_timer = state[6]
        assert(len(state[7]) == 1)
        cur_data.ST.main_SSD = state[7]
        assert(len(state[8]) == 4)
        cur_data.ST.main_free_space = state[8]
        for i in range(9, 20):  #一个循环多个检查
            assert(len(state[i]) == 1)
        cur_data.ST.main_GPS = state[9]
        cur_data.ST.main_door = state[10]
        cur_data.ST.human_near = state[11]
        cur_data.ST.solar_pad = state[12]
        cur_data.ST.temp_sr = state[13]
        cur_data.ST.hum_sr = state[14]
        cur_data.ST.wind_dir_sr = state[15]
        cur_data.ST.wind_speed_sr = state[16]
        cur_data.ST.rain_sr = state[17]
        cur_data.ST.road_temp_sr = state[18]
        cur_data.ST.base_temp_sr = state[19]
        
        assert(len(state[20]) == 6)
        cur_data.ST.road_state_sr = state[20]
        cur_data.ST.vis_sr = state[21] + " " + state[22][: len(state[22]) - 1]
        
        cur_data.EOF = line_data[2]
    except IndexError:
        print("Error: missing parameters")
        return False, DataFile()
    except AssertionError:
        print("Error: parameters unmatched")
        return False, DataFile()    
    return True, cur_data



def cal_rain(cur_data: DataFile):
    res = 0
    rain_data = cur_data.MR.rain_hour_minute
    for i in range(0, len(rain_data), 2):
        cur = rain_data[i: i + 2]
        if cur != "--":
            res += int(cur)
    res /= 10.0
    return res



def exam_quality(all_data_file):
    all_bad_QC = {}
    for i in range(len(all_data_file)):
        cur_data: DataFile = all_data_file[i]
        timestamp = cur_data.basic_ifo.observe_time[8: 12]
        all_bad_QC[timestamp] = []  #为所有时刻记录不好的事件
        water_P = float(cur_data.TH.pressure) / 10.0
        if water_P < 0:
            all_bad_QC[timestamp].append("pressure can't be negative")
        if water_P > 70:
            all_bad_QC[timestamp].append("pressure too high")
        temp = float(cur_data.TH.temperature) / 10.0
        if temp < -80:
            all_bad_QC[timestamp].append("temperature too low")
        if temp > 60:
            all_bad_QC[timestamp].append("temperature too high")
        dew_temp = float(cur_data.TH.dew_temp) / 10.0
        if dew_temp < -80:
            all_bad_QC[timestamp].append("dew temp too low")
        if dew_temp > 35:
            all_bad_QC[timestamp].append("dew temp too high")
        ground_temp = float(cur_data.RT.road_temp) / 10.0
        if ground_temp < -80:
            all_bad_QC[timestamp].append("ground temp too low")
        if ground_temp > 80:
            all_bad_QC[timestamp].append("ground temp too high")
        
        wind2 = float(cur_data.WI.avg_speed2) / 10.0
        wind10 = float(cur_data.WI.avg_speed10) / 10.0
        if wind2 < 0 or wind10 < 0:
            all_bad_QC[timestamp].append("wind speed can't be negative")
        if wind2 > 75 or wind10 > 75:
            all_bad_QC[timestamp].append("wind speed too high")
        rsc_wind = float(cur_data.WI.rsc_speed) / 10.0
        if rsc_wind < 0:
            all_bad_QC[timestamp].append("rsc wind speed can't be negative")
        if rsc_wind > 150:
            all_bad_QC[timestamp].append("rsc wind speed too high")

        hour_rain = cal_rain(cur_data)   
        if hour_rain < 0:
            all_bad_QC[timestamp].append("rain can't be negative")
        if hour_rain > 240:
            all_bad_QC[timestamp].append("rain too much")
        hum = float(cur_data.TH.hum)
        if hum < 0:
            all_bad_QC[timestamp].append("hum can't be negative")
        if hum > 100:
            all_bad_QC[timestamp].append("hum exceed range")
        
        if i >= 2:
            pre_data: DataFile = all_data_file[i - 2]   #获取两分钟前的数据
            pre_temp = float(pre_data.TH.temperature) / 10.0
            if abs(temp - pre_temp) > 3:
                all_bad_QC[timestamp].append("temp change too much")
            pre_dew = float(pre_data.TH.dew_temp) / 10.0
            if abs(dew_temp - pre_dew) > 2:
                all_bad_QC[timestamp].append("dew change too much")
            pre_road = float(pre_data.RT.road_temp) / 10.0
            if abs(ground_temp - pre_road) > 0.5:
                all_bad_QC[timestamp].append("ground temp change too much")
            pre_hum = float(pre_data.TH.hum)
            if abs(hum - pre_hum) > 10:
                all_bad_QC[timestamp].append("relative hum change too much")
            pre_wind2 = float(pre_data.WI.avg_speed2) / 10.0
            if abs(wind2 - pre_wind2) > 20:
                all_bad_QC[timestamp].append("wind speed change too much")
    return all_bad_QC

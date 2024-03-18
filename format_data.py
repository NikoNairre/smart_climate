class StationIfo:
    id = None
    observe_time = None
    latitude = None     #经度
    longitude = None    #纬度
    altitude = None
    QC_flag = None       #质控
    def __init__(self) -> None:
        pass

class Temp_Hum:
    temperature = None
    high_temp = None
    high_temp_time = None
    low_temp = None
    low_temp_time = None
    dew_temp = None     #露点温度
    hum = None  #相对湿度
    low_hum = None
    low_hum_time = None
    pressure = None
    def __init__(self) -> None:
        pass

class Rain:
    rain_sum = None 
    def __init__(self) -> None:
        pass

class Wind:
    wind_dir2 = None
    avg_speed2 = None
    wind_dir10 = None
    avg_speed10 = None
    high_wind_dir = None    #最大用了high,极大用max
    high_wind_speed = None
    high_speed_time = None
    rsc_dir = None      #瞬时风向
    rsc_speed = None
    max_dir = None  #极大方向
    max_speed = None
    max_speed_time = None
    
    max_dir_minute = None
    max_speed_minute = None
    max_speed_time_minute = None
    def __init__(self) -> None:
        pass

class RoadTemp:
    road_temp = None
    road_high_temp = None
    road_high_temp_time = None
    road_low_temp = None
    road_low_temp_time = None
    base_temp = None
    def __init__(self) -> None:
        pass

class Visibility:
    avg_vis_minute = None
    low_vis = None
    low_vis_time = None
    def __init__(self) -> None:
        pass

class RoadState:
    road_state = None
    snow_thick = None
    water_thick = None
    ice_thick = None
    ice_temp = None
    deicer_con = None   #融雪剂浓度
    def __init__(self) -> None:
        pass

class WeatherState:
    weather_code = None
    def __init__(self) -> None:
        pass

class RainHourMinute:
    rain_hour_minute = None
    def __init__(self) -> None:
        pass
class QC_State:
    Q1 = None   #单站级
    Q2 = None   #省级
    Q3 = None   #国家级
    def __init__(self) -> None:
        pass
# a = StationIfo()
# a.id = 2
# print(a.id)


class DataFile:
    def __init__(self, index) -> None:
        self.index = index
        self.basic_ifo = StationIfo()
        self.TH = Temp_Hum()
        self.RE = Rain()
        self.WI = Wind()
        self.RT = RoadTemp()
        self.VV = Visibility()
        self.RS = RoadState()
        self.WW = WeatherState()
        self.MR = RainHourMinute()
        self.QC = QC_State()
        self.EOF = None      #文件结束符
    #放在__init__外面会导致所有DataFile类共享这些属性，造成数据错误


class StateData:
    main_state = None
    main_volt = None    #电压
    main_power_type = None
    main_cpu_temp = None
    main_AD = None
    main_timer = None
    main_SSD = None
    main_free_space = None
    main_GPS = None
    main_door = None
    human_near = None
    solar_pad = None
    temp_sr = None      #温度传感器
    hum_sr = None
    wind_dir_sr = None
    wind_speed_sr = None
    rain_sr = None
    road_temp_sr = None
    base_temp_sr = None
    road_state_sr = None
    vis_sr = None   #能见度状态
    def __init__(self) -> None:
        pass

class StateFile:
    def __init__(self, index) -> None:
        self.index = index
        self.basic_ifo = StationIfo()
        self.ST = StateData()
        self.EOF = None
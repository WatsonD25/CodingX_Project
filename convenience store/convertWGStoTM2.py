from pyproj import Transformer

def WGStoTM2(lon,lat):
  transformer = Transformer.from_crs("epsg:4326","epsg:3826")
  lon_tm2,lat_tm2=transformer.transform(lat,lon)
  return [lon_tm2,lat_tm2] #前面是緯度 後面是經度


# 請分別輸入經度及緯度,將輸出一個list為TWD97TM2的座標([0]為經度方向,[1]為緯度方向)
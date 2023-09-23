# Precaution of importing in Python

在import函式時，務必要注意路徑的有效性，尤其是絕對路徑。
當編輯器報錯時，就要馬上改掉，要是該絕對路徑存在於某個外部函式包裡面，replit就會自動安裝，讓命名空間亂成一團。
隨時注意目錄裡面有沒有`.pythonlib/`，或觀察裡面的函式包名稱。
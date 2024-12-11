import math

def euclideanDistance(point1, point2):

  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Örnek noktalar
points = [(1, 2), (4, 6), (2, 3), (5, 1)]

# Tüm noktalar arasındaki mesafeleri hesapla
distances = []
for i in range(len(points)):
  for j in range(i+1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)

# Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
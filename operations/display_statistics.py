"""
COMP 348: Assignment 2
Name: Asifur Rahman
Student ID: 40194283
"""

import math
import random


def show_global(data):
    base_stations = data['baseStations']
    num_stations = len(base_stations)
    num_ants = sum(len(bs['ants']) for bs in base_stations)
    per_num_ants = [len(bs['ants']) for bs in base_stations]

    max_ants = max(per_num_ants)
    min_ants = min(per_num_ants)
    avg_ants = num_ants / num_stations

    covered_points = {}
    total_points = set()

    max_covered_points = 0
    max_antenna_name = None

    for bs in base_stations:
        for ant in bs['ants']:
            covered_count = 0
            for points in ant['pts']:
                coordinates = (points[0], points[1])
                total_points.add(coordinates)
                if coordinates not in covered_points:
                    covered_points[coordinates] = 0
                covered_points[coordinates] += 1
                covered_count += 1

            if covered_count > max_covered_points:
                max_covered_points = covered_count
                max_antenna_name = (ant['id'], bs['id'])

    points_covered_by_one = sum(1 for count in covered_points.values() if count == 1)
    points_covered_by_many = sum(1 for count in covered_points.values() if count > 1)
    min_lat = data['min_lat']
    max_lat = data['max_lat']
    min_lon = data['min_lon']
    max_lon = data['max_lon']
    step = data['step']

    total_possible_points = math.ceil((((max_lat - min_lat) / step) + 1) * (((max_lon - min_lon) / step) + 1))
    uncovered_points = total_possible_points - len(covered_points)
    ant_max_coverage = max(covered_points.values())
    ant_avg_coverage = sum(covered_points.values()) / len(covered_points)
    coverage_percentage = (len(covered_points) / total_possible_points) * 100

    print(f"Total number of base stations: {num_stations}")
    print(f"Total number of antennas: {num_ants}")
    print(f"The max, min and average of antennas per BS: {max_ants}, {min_ants}, {avg_ants}")
    print(f"Total number of points covered by exactly one antenna: {points_covered_by_one}")
    print(f"Total number of points covered by more than one antenna: {points_covered_by_many}")
    print(f"Total number of points not covered by any antenna: {uncovered_points}")
    print(f"Maximum number of antennas covering one point: {ant_max_coverage}")
    print(f"Average number of antennas covering a point: {ant_avg_coverage:.2f}")
    print(f"Percentage of the covered area: {coverage_percentage:.2f}%")
    print(f"ID of the base station, antenna with max coverage: Base station {max_antenna_name[1]}, Antenna {max_antenna_name[0]}")


def show_random_station_statistics(data):
    base_stations = data['baseStations']
    if not base_stations:
        print("No base stations available.")
        return

    random_station = random.choice(base_stations)
    show_station_statistics(random_station)


def show_station_statistics_by_id(data, station_id):
    base_stations = data['baseStations']
    station = next((bs for bs in base_stations if bs['id'] == station_id), None)
    if station:
        show_station_statistics(station)
    else:
        print(f"Base station with ID {station_id} not found.")


def show_station_statistics(station):
    print(f"Base Station ID: {station['id']}")
    print(f"Location: ({station['lat']}, {station['lon']})")
    print(f"Number of Antennas: {len(station['ants'])}")
    for ant in station['ants']:
        print(f"  Antenna ID: {ant['id']}")
        print(f"    Frequency: {ant['frq']}")
        print(f"    Bandwidth: {ant['bw']}")
        print(f"    Points: {ant['pts']}")


def show_coverage(data, lat, lon):
    covered_stations = []
    base_stations = data['baseStations']

    for bs in base_stations:
        for ant in bs['ants']:
            for point in ant['pts']:
                if point[0] == lat and point[1] == lon:
                    covered_stations.append({
                        "station_id": bs['id'],
                        "antenna_id": ant['id'],
                        "signal": point[2]
                    })

    if covered_stations:
        print(f"The point ({lat}, {lon}) is covered by the following base stations and antennas:")
        for station in covered_stations:
            print(f"Base Station ID: {station['base_station_id']}, "
                  f"Antenna ID: {station['antenna_id']}, "
                  f"Received Power: {station['received_power']}")
    else:
        nearest_station = None
        min_distance = float('inf')
        for bs in base_stations:
            for ant in bs['ants']:
                for point in ant['pts']:
                    current_distance = distance(lat, lon, point[0], point[1])
                    if min_distance > current_distance:
                        min_distance = current_distance
                        nearest_station = {
                            "station_id": bs['id'],
                            "antenna_id": ant['id'],
                            "coordinates": (point[0], point[1]),
                            "signal": point[2]
                        }

        if nearest_station:
            print(f"The point ({lat}, {lon}) is not covered by the antennas. The nearest stations is:")
            print(f"Base Station ID: {nearest_station['station_id']}, "
                  f"Antenna ID: {nearest_station['antenna_id']}, "
                  f"Coordinates: {nearest_station['coordinates']}, "
                  f"Signal Strength: {nearest_station['signal']}")


def distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

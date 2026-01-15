#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flask Web Application untuk Sistem Pakar Mitigasi Bencana Alam - ENHANCED VERSION
Implementasi Logika Matematika dengan Multiple Variables
Mendukung: Banjir, Gempa, Status Air, dan lainnya
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from typing import Dict, Tuple, List
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Debug: Print environment variable status
api_key_debug = os.getenv('OPENWEATHER_API_KEY')
print("\n" + "="*60)
print("🔍 DEBUG: Environment Variables")
print("="*60)
print(f"Current Working Directory: {os.getcwd()}")
print(f"API Key Status: {'✅ SET' if api_key_debug else '❌ NOT SET'}")
if api_key_debug:
    print(f"API Key Length: {len(api_key_debug)} characters")
    print(f"API Key Preview: {api_key_debug[:10]}...{api_key_debug[-10:]}")
else:
    print("⚠️  WARNING: OPENWEATHER_API_KEY not found in environment!")
    print("   Check if .env file exists in current directory")
print("="*60 + "\n")

app = Flask(__name__)
CORS(app)

# ============================================
# ENHANCED PROPOSITIONAL LOGIC ENGINE
# ============================================

def AND(*args: bool) -> bool:
    """AND Gate - Returns True only if all inputs are True"""
    return all(args)

def OR(*args: bool) -> bool:
    """OR Gate - Returns True if at least one input is True"""
    return any(args)

def NOT(a: bool) -> bool:
    """NOT Gate - Returns opposite of input"""
    return not a

def calculate_flood_risk(p: bool, q: bool, r: bool) -> Tuple[bool, bool]:
    """
    Flood Risk Calculation (3 Variables)
    Formula: FLOOD = p ∧ (q ∨ r)
    
    Args:
        p: High Rainfall (Curah Hujan Tinggi)
        q: Deforestation (Alih Fungsi Lahan Sawit)
        r: Bad Drainage (Sungai Dangkal/Sempit)
    
    Returns:
        Tuple of (q_or_r, flood_result)
    """
    q_or_r = OR(q, r)
    flood_result = AND(p, q_or_r)
    return q_or_r, flood_result

def calculate_earthquake_risk(e: bool, b: bool, l: bool) -> Tuple[bool, bool]:
    """
    Earthquake Risk Calculation
    Formula: QUAKE = e ∧ (b ∨ l)
    
    Args:
        e: Seismic Activity (Aktivitas Seismik)
        b: Building Quality Poor (Kualitas Bangunan Buruk)
        l: Landslide Prone Area (Daerah Rawan Longsor)
    
    Returns:
        Tuple of (b_or_l, quake_result)
    """
    b_or_l = OR(b, l)
    quake_result = AND(e, b_or_l)
    return b_or_l, quake_result

def calculate_combined_risk(flood: bool, quake: bool) -> Dict[str, any]:
    """
    Calculate combined disaster risk
    
    Returns:
        Dictionary with risk levels and recommendations
    """
    if flood and quake:
        return {
            'level': 'CRITICAL',
            'severity': 5,
            'color': 'red-900',
            'icon': 'fa-skull-crossbones',
            'title': '🔴 BAHAYA EKSTREM - MULTI BENCANA',
            'description': 'Risiko banjir DAN gempa terdeteksi bersamaan!'
        }
    elif flood:
        return {
            'level': 'HIGH',
            'severity': 4,
            'color': 'red-600',
            'icon': 'fa-water',
            'title': '🚨 PERINGATAN BANJIR',
            'description': 'Risiko banjir tinggi terdeteksi'
        }
    elif quake:
        return {
            'level': 'HIGH',
            'severity': 4,
            'color': 'orange-600',
            'icon': 'fa-house-crack',
            'title': '⚠️ PERINGATAN GEMPA',
            'description': 'Risiko gempa bumi terdeteksi'
        }
    else:
        return {
            'level': 'SAFE',
            'severity': 1,
            'color': 'green-600',
            'icon': 'fa-shield-alt',
            'title': '✅ KONDISI AMAN',
            'description': 'Tidak ada risiko bencana terdeteksi'
        }

# ============================================
# RECOMMENDATION ENGINE
# ============================================

def get_flood_recommendation(p: bool, q: bool, r: bool, result: bool) -> Dict[str, str]:
    """Generate flood-specific recommendations"""
    if not result:
        return {
            'icon': 'fa-check-circle',
            'color': 'text-green-600',
            'title': '✅ Tidak Ada Risiko Banjir',
            'text': 'Kondisi saat ini aman dari risiko banjir.\nTetap lakukan pemantauan rutin.'
        }
    
    # All three factors active (p=T, q=T, r=T)
    if p and q and r:
        return {
            'icon': 'fa-exclamation-triangle',
            'color': 'text-red-700',
            'title': '🔴 BAHAYA BANJIR MAKSIMAL',
            'text': 'Semua faktor risiko aktif!\n'
                   'TINDAKAN:\n'
                   '- Evakuasi segera ke tempat tinggi\n'
                   '- Matikan listrik dan gas\n'
                   '- Bawa dokumen penting\n'
                   '- Ikuti instruksi petugas'
        }
    # High rainfall with land damage (p=T, q=T, r=F)
    elif p and q and not r:
        return {
            'icon': 'fa-tree',
            'color': 'text-orange-600',
            'title': '⚠️ RISIKO BANJIR - FAKTOR LAHAN',
            'text': 'Curah hujan tinggi dengan kerusakan lahan.\n'
                   'TINDAKAN:\n'
                   '- Siaga evakuasi\n'
                   '- Pantau daerah deforestasi\n'
                   '- Hindari area rawan longsor'
        }
    # High rainfall with bad drainage (p=T, q=F, r=T)
    elif p and not q and r:
        return {
            'icon': 'fa-water',
            'color': 'text-orange-600',
            'title': '⚠️ RISIKO BANJIR - FAKTOR DRAINASE',
            'text': 'Curah hujan tinggi dengan drainase buruk.\n'
                   'TINDAKAN:\n'
                   '- Siaga evakuasi\n'
                   '- Pantau ketinggian sungai\n'
                   '- Siapkan jalur evakuasi'
        }
    else:
        return {
            'icon': 'fa-exclamation',
            'color': 'text-yellow-600',
            'title': '⚠️ WASPADA BANJIR',
            'text': 'Beberapa faktor risiko terdeteksi.\n'
                   'Tingkatkan kewaspadaan dan siapkan rencana evakuasi.'
        }

def get_earthquake_recommendation(e: bool, b: bool, l: bool, result: bool) -> Dict[str, str]:
    """Generate earthquake-specific recommendations"""
    if not result:
        return {
            'icon': 'fa-check-circle',
            'color': 'text-green-600',
            'title': '✅ Tidak Ada Risiko Gempa',
            'text': 'Tidak ada aktivitas seismik signifikan.\nTetap siaga dan waspada.'
        }
    
    if e and b and l:
        return {
            'icon': 'fa-house-crack',
            'color': 'text-red-700',
            'title': '🔴 BAHAYA GEMPA MAKSIMAL',
            'text': 'Aktivitas seismik tinggi dengan bangunan rentan.\n'
                   'TINDAKAN:\n'
                   '- Keluar dari bangunan\n'
                   '- Hindari area longsor\n'
                   '- Ke tempat terbuka\n'
                   '- Siaga tsunami jika dekat pantai'
        }
    elif e and b:
        return {
            'icon': 'fa-building',
            'color': 'text-orange-600',
            'title': '⚠️ RISIKO KERUSAKAN BANGUNAN',
            'text': 'Gempa dengan bangunan berkualitas buruk.\n'
                   'TINDAKAN:\n'
                   '- Evakuasi dari bangunan\n'
                   '- Hindari struktur tinggi\n'
                   '- Ke area terbuka'
        }
    elif e and l:
        return {
            'icon': 'fa-mountain',
            'color': 'text-orange-600',
            'title': '⚠️ RISIKO TANAH LONGSOR',
            'text': 'Gempa di area rawan longsor.\n'
                   'TINDAKAN:\n'
                   '- Jauhi lereng bukit\n'
                   '- Hindari jurang\n'
                   '- Evakuasi ke dataran'
        }
    else:
        return {
            'icon': 'fa-exclamation',
            'color': 'text-yellow-600',
            'title': '⚠️ WASPADA GEMPA',
            'text': 'Aktivitas seismik terdeteksi.\nTingkatkan kewaspadaan.'
        }

# ============================================
# TRUTH TABLE GENERATION
# ============================================

def generate_flood_truth_table() -> list:
    """Generate complete flood truth table (8 combinations for 3 variables)"""
    table = []
    for i in range(8):
        p = bool(i & 4)
        q = bool(i & 2)
        r = bool(i & 1)
        
        q_or_r, result = calculate_flood_risk(p, q, r)
        
        table.append({
            'p': p, 'q': q, 'r': r,
            'q_or_r': q_or_r,
            'result': result
        })
    
    return table

def generate_earthquake_truth_table() -> list:
    """Generate earthquake truth table (8 combinations for 3 variables)"""
    table = []
    for i in range(8):
        e = bool(i & 4)
        b = bool(i & 2)
        l = bool(i & 1)
        
        b_or_l, result = calculate_earthquake_risk(e, b, l)
        
        table.append({
            'e': e, 'b': b, 'l': l,
            'b_or_l': b_or_l,
            'result': result
        })
    
    return table

# ============================================
# WEATHER API INTEGRATION
# ============================================

def get_weather_data(city: str = None, lat: float = None, lon: float = None) -> Dict:
    """
    Get weather data from OpenWeatherMap API
    
    Args:
        city: City name (optional)
        lat: Latitude (optional)
        lon: Longitude (optional)
    
    Returns:
        Dictionary with weather data
    """
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    if not api_key:
        return {
            'success': False,
            'error': 'API key not configured. Please set OPENWEATHER_API_KEY in .env file'
        }
    
    # Use provided coordinates or default to Banda Aceh
    if not lat or not lon:
        if not city:
            city = os.getenv('DEFAULT_CITY', 'Banda Aceh')
        lat = float(os.getenv('DEFAULT_LAT', '5.5483'))
        lon = float(os.getenv('DEFAULT_LON', '95.3238'))
    
    try:
        # Current weather - reduced timeout
        current_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=id'
        current_response = requests.get(current_url, timeout=5)
        current_response.raise_for_status()
        current_data = current_response.json()
        
        # 5-day forecast - reduced timeout
        forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=id'
        forecast_response = requests.get(forecast_url, timeout=5)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()
        
        # Process forecast data (get daily forecast)
        daily_forecast = []
        processed_dates = set()
        
        for item in forecast_data['list'][:40]:  # 5 days * 8 (3-hour intervals)
            date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
            
            if date not in processed_dates and len(daily_forecast) < 5:
                daily_forecast.append({
                    'date': date,
                    'day': datetime.fromtimestamp(item['dt']).strftime('%A'),
                    'temp': round(item['main']['temp']),
                    'temp_min': round(item['main']['temp_min']),
                    'temp_max': round(item['main']['temp_max']),
                    'description': item['weather'][0]['description'].capitalize(),
                    'icon': item['weather'][0]['icon'],
                    'humidity': item['main']['humidity'],
                    'wind_speed': round(item['wind']['speed'] * 3.6, 1),  # Convert m/s to km/h
                    'rain': item.get('rain', {}).get('3h', 0)
                })
                processed_dates.add(date)
        
        # Calculate flood risk based on weather
        rainfall = current_data.get('rain', {}).get('1h', 0)
        humidity = current_data['main']['humidity']
        
        # Simple flood risk assessment based on weather
        flood_risk_level = 'low'
        if rainfall > 50 or humidity > 90:
            flood_risk_level = 'high'
        elif rainfall > 20 or humidity > 80:
            flood_risk_level = 'medium'
        
        return {
            'success': True,
            'location': {
                'name': current_data['name'],
                'country': current_data['sys']['country'],
                'lat': lat,
                'lon': lon
            },
            'current': {
                'temp': round(current_data['main']['temp']),
                'feels_like': round(current_data['main']['feels_like']),
                'temp_min': round(current_data['main']['temp_min']),
                'temp_max': round(current_data['main']['temp_max']),
                'pressure': current_data['main']['pressure'],
                'humidity': current_data['main']['humidity'],
                'description': current_data['weather'][0]['description'].capitalize(),
                'icon': current_data['weather'][0]['icon'],
                'wind_speed': round(current_data['wind']['speed'] * 3.6, 1),  # Convert m/s to km/h
                'wind_deg': current_data['wind'].get('deg', 0),
                'clouds': current_data['clouds']['all'],
                'visibility': current_data.get('visibility', 10000) / 1000,  # Convert to km
                'rain_1h': current_data.get('rain', {}).get('1h', 0),
                'rain_3h': current_data.get('rain', {}).get('3h', 0),
                'sunrise': datetime.fromtimestamp(current_data['sys']['sunrise']).strftime('%H:%M'),
                'sunset': datetime.fromtimestamp(current_data['sys']['sunset']).strftime('%H:%M'),
                'timestamp': datetime.fromtimestamp(current_data['dt']).strftime('%Y-%m-%d %H:%M:%S')
            },
            'forecast': daily_forecast,
            'flood_risk': {
                'level': flood_risk_level,
                'rainfall': rainfall,
                'message': get_flood_risk_message(flood_risk_level, rainfall)
            }
        }
        
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f'Failed to fetch weather data: {str(e)}'
        }
    except Exception as e:
        return {
            'success': False,
            'error': f'Error processing weather data: {str(e)}'
        }

def get_flood_risk_message(level: str, rainfall: float) -> str:
    """Get flood risk message based on weather conditions"""
    if level == 'high':
        return f'⚠️ PERINGATAN: Curah hujan tinggi ({rainfall}mm/jam). Waspada potensi banjir!'
    elif level == 'medium':
        return f'⚡ PERHATIAN: Curah hujan sedang ({rainfall}mm/jam). Pantau kondisi cuaca.'
    else:
        return '✅ Kondisi cuaca normal. Tidak ada peringatan banjir.'

# ============================================
# FLASK ROUTES
# ============================================

@app.route('/')
def index():
    """Serve the main web interface"""
    return render_template('index_enhanced.html')

@app.route('/api/calculate-flood', methods=['POST'])
def api_calculate_flood():
    """Calculate flood risk"""
    try:
        data = request.get_json()
        p = bool(data.get('p', False))
        q = bool(data.get('q', False))
        r = bool(data.get('r', False))
        
        q_or_r, result = calculate_flood_risk(p, q, r)
        recommendation = get_flood_recommendation(p, q, r, result)
        
        return jsonify({
            'success': True,
            'variables': {'p': p, 'q': q, 'r': r},
            'steps': {
                'q_or_r': q_or_r
            },
            'result': result,
            'recommendation': recommendation
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/calculate-earthquake', methods=['POST'])
def api_calculate_earthquake():
    """Calculate earthquake risk"""
    try:
        data = request.get_json()
        e = bool(data.get('e', False))
        b = bool(data.get('b', False))
        l = bool(data.get('l', False))
        
        b_or_l, result = calculate_earthquake_risk(e, b, l)
        recommendation = get_earthquake_recommendation(e, b, l, result)
        
        return jsonify({
            'success': True,
            'variables': {'e': e, 'b': b, 'l': l},
            'steps': {'b_or_l': b_or_l},
            'result': result,
            'recommendation': recommendation
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/calculate-combined', methods=['POST'])
def api_calculate_combined():
    """Calculate combined disaster risk"""
    try:
        data = request.get_json()
        
        # Flood variables
        p = bool(data.get('p', False))
        q = bool(data.get('q', False))
        r = bool(data.get('r', False))
        
        # Earthquake variables
        e = bool(data.get('e', False))
        b = bool(data.get('b', False))
        l = bool(data.get('l', False))
        
        # Calculate both risks
        q_or_r, flood_result = calculate_flood_risk(p, q, r)
        b_or_l, quake_result = calculate_earthquake_risk(e, b, l)
        
        # Get combined risk assessment
        combined_risk = calculate_combined_risk(flood_result, quake_result)
        
        # Get specific recommendations
        flood_rec = get_flood_recommendation(p, q, r, flood_result)
        quake_rec = get_earthquake_recommendation(e, b, l, quake_result)
        
        return jsonify({
            'success': True,
            'flood': {
                'variables': {'p': p, 'q': q, 'r': r},
                'result': flood_result,
                'recommendation': flood_rec
            },
            'earthquake': {
                'variables': {'e': e, 'b': b, 'l': l},
                'result': quake_result,
                'recommendation': quake_rec
            },
            'combined_risk': combined_risk
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/truth-table/flood', methods=['GET'])
def api_flood_truth_table():
    """Get flood truth table"""
    try:
        table = generate_flood_truth_table()
        return jsonify({'success': True, 'table': table})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/truth-table/earthquake', methods=['GET'])
def api_earthquake_truth_table():
    """Get earthquake truth table"""
    try:
        table = generate_earthquake_truth_table()
        return jsonify({'success': True, 'table': table})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/weather', methods=['GET'])
def api_weather():
    """Get current weather and forecast"""
    try:
        city = request.args.get('city')
        lat = request.args.get('lat', type=float)
        lon = request.args.get('lon', type=float)
        
        weather_data = get_weather_data(city=city, lat=lat, lon=lon)
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/weather/search', methods=['GET'])
def api_weather_search():
    """Search for city coordinates with Indonesia priority and exact match"""
    try:
        city = request.args.get('city', '').strip()
        api_key = os.getenv('OPENWEATHER_API_KEY')
        
        if not api_key:
            return jsonify({
                'success': False,
                'error': 'Kunci API tidak dikonfigurasi'
            }), 400
        
        if not city:
            return jsonify({
                'success': False,
                'error': 'Parameter kota diperlukan'
            }), 400
        
        city_lower = city.lower()
        all_cities = []
        
        print(f"\n🔍 Searching for city: '{city}'")
        
        # Strategy 1: Search with Indonesia country code first (highest priority)
        try:
            url_id = f'https://api.openweathermap.org/geo/1.0/direct?q={city},ID&limit=10&appid={api_key}'
            response_id = requests.get(url_id, timeout=3)
            if response_id.ok:
                data_id = response_id.json()
                print(f"📍 Found {len(data_id)} results from Indonesia search")
                for item in data_id:
                    is_exact_match = item['name'].lower() == city_lower
                    all_cities.append({
                        'name': item['name'],
                        'country': item['country'],
                        'state': item.get('state', ''),
                        'lat': item['lat'],
                        'lon': item['lon'],
                        'priority': 0 if is_exact_match else 1,  # Exact match = highest priority
                        'match_score': 100 if is_exact_match else 50
                    })
        except Exception as e:
            print(f"❌ Indonesia search error: {e}")
        
        # Strategy 2: Global search (lower priority)
        if len(all_cities) < 5:
            try:
                url_global = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=15&appid={api_key}'
                response_global = requests.get(url_global, timeout=3)
                if response_global.ok:
                    data_global = response_global.json()
                    print(f"🌍 Found {len(data_global)} results from global search")
                    for item in data_global:
                        # Skip if already added
                        if not any(c['lat'] == item['lat'] and c['lon'] == item['lon'] for c in all_cities):
                            is_exact_match = item['name'].lower() == city_lower
                            is_indonesia = item['country'] == 'ID'
                            
                            # Priority: exact match ID > exact match other > ID cities > others
                            if is_exact_match and is_indonesia:
                                priority = 0
                                score = 100
                            elif is_exact_match:
                                priority = 1
                                score = 90
                            elif is_indonesia:
                                priority = 2
                                score = 60
                            else:
                                priority = 3
                                score = 30
                            
                            all_cities.append({
                                'name': item['name'],
                                'country': item['country'],
                                'state': item.get('state', ''),
                                'lat': item['lat'],
                                'lon': item['lon'],
                                'priority': priority,
                                'match_score': score
                            })
            except Exception as e:
                print(f"❌ Global search error: {e}")
        
        # Sort by priority and match score, then limit to 5
        all_cities.sort(key=lambda x: (x['priority'], -x['match_score'], x['name']))
        
        print(f"✅ Total unique cities found: {len(all_cities)}")
        if all_cities:
            print(f"🏆 Top result: {all_cities[0]['name']}, {all_cities[0]['country']} (priority: {all_cities[0]['priority']}, score: {all_cities[0]['match_score']})")
        
        cities = [
            {
                'name': c['name'],
                'country': c['country'],
                'state': c['state'],
                'lat': c['lat'],
                'lon': c['lon']
            }
            for c in all_cities[:5]
        ]
        
        if not cities:
            print(f"❌ No cities found for: '{city}'")
            return jsonify({
                'success': False,
                'error': f'Kota "{city}" tidak ditemukan'
            }), 404
        
        return jsonify({'success': True, 'cities': cities})
        
    except requests.exceptions.Timeout:
        return jsonify({'success': False, 'error': 'Koneksi timeout. Coba lagi.'}), 408
    except requests.exceptions.RequestException as e:
        return jsonify({'success': False, 'error': f'Gagal terhubung ke server: {str(e)}'}), 500
    except Exception as e:
        print(f"❌ Search error: {e}")
        return jsonify({'success': False, 'error': f'Terjadi kesalahan: {str(e)}'}), 400

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check"""
    return jsonify({
        'status': 'healthy',
        'service': 'Sistem Pakar Mitigasi Bencana Alam - Enhanced',
        'version': '2.0.0',
        'features': ['flood', 'earthquake', 'combined']
    })

# ============================================
# ERROR HANDLERS
# ============================================

@app.route('/debug-static')
def debug_static():
    """Debug endpoint to check static files on server"""
    try:
        current_dir = os.getcwd()
        files_root = os.listdir(current_dir)
        
        static_info = "Static folder not found"
        team_images = []
        
        static_path = os.path.join(current_dir, 'static')
        if os.path.exists(static_path):
            static_info = os.listdir(static_path)
            
            team_path = os.path.join(static_path, 'images', 'team')
            if os.path.exists(team_path):
                team_images = os.listdir(team_path)
            else:
                team_images = "Team folder not found"
        
        return jsonify({
            'current_dir': current_dir,
            'root_files': files_root,
            'static_contents': static_info,
            'team_images': team_images,
            'env_vars': dict(os.environ)
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'error': 'Internal server error'}), 500

# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    
    print("=" * 80)
    print("🌊 SISTEM PAKAR MITIGASI BENCANA ALAM - ENHANCED VERSION 🌊".center(80))
    print("=" * 80)
    print()
    print("✨ NEW FEATURES:")
    print("   - Multi-disaster support (Banjir + Gempa)")
    print("   - Enhanced variables (7 total)")
    print("   - Combined risk assessment")
    print("   - Improved recommendations")
    print()
    print("🚀 Starting Flask server...")
    print("📍 Server: http://localhost:5000")
    print("📍 API Endpoints:")
    print("   - POST /api/calculate-flood")
    print("   - POST /api/calculate-earthquake")
    print("   - POST /api/calculate-combined")
    print("   - GET  /api/truth-table/flood")
    print("   - GET  /api/truth-table/earthquake")
    print("   - GET  /api/weather")
    print("   - GET  /api/weather/search")
    print()
    print("Press CTRL+C to stop")
    print("=" * 80)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
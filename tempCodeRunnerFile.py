
    elif data_type == 'ebay':
        scrape_data = scrape_ebay_product(url)
    
    elif data_type == 'news':
        scrape_data = scrape_news_headlines(url)

    if not scrape_data:
        return jsonify({'success': False, 'error': 'No data found.'})
    
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(api_link, json=scrape_data, headers=headers)
        response.raise_for_status()
        return jsonify({'success': True, 'message': 'Data sent to API successfully.'})
    except requests.exceptions.RequestException as e:
        return jsonify({'success': False, 'error': str(e)})
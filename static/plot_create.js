function googlePlotCreate(){
    const price_trace = {
        x: twitter_hourly_time,
        y: hourly_price_data,
        name: 'Price',
        line: {
            color: "grey", width: 1
        }
    };
    const google_trace = {
        x: google_time,
        y: google_comments,
        name: 'Trends',
        yaxis: 'y2',
        line: {
            color: "#0F9D58", width: 1.5
        }
    };
    const layout = {
        title: 'Google',
        autosize: false,
        height: 300,
        width: 600,
        margin: {r: 0, l: 20, b: 0, t: 30},
	    legend: {
            "orientation": "h", x: 0.4, y: -0.1
        },
        yaxis1: {
            visible: false,
        },
        yaxis2: {
            overlaying: 'y',
            zeroline: false,
        }
    };
    Plotly.newPlot('google_div', [price_trace, google_trace], layout, {displayModeBar: false}, {responsive: true});
}

function TwitterPlotCreate(){
    const tweets_bar1 = {
        visible: false,
        x: twitter_daily_time,
        y: twitter_daily_data[3],
        name: '#Bitcoin',
        type: 'bar',
        connectgaps: true,
        hovertemplate: ' %{x},%{y} (#Bitcoin)<extra></extra>',
        marker: {color: '#03045e'}
    };
    const tweets_bar2 = {
        visible: false,
        x: twitter_daily_time,
        y: twitter_daily_data[1],
        name: '#BTC',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (#BTC)<extra></extra>',
        marker: {color: '#0077b6'}
    };
    const tweets_bar3 = {
        visible: false,
        x: twitter_daily_time,
        y: twitter_daily_data[0],
        name: 'BTC',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (BTC)<extra></extra>',
        marker: {color: '#00b4d8'}
    };
    const tweets_bar4 = {
        visible: false,
        x: twitter_daily_time,
        y: twitter_daily_data[2],
        name: 'Bitcoin',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (Bitcoin)<extra></extra>',
        marker: {color: '#90e0ef'}
    };
    const tweets_bar5 = {
        x: twitter_hourly_time,
        y: twitter_hourly_data[3],
        name: '#Bitcoin',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (#Bitcoin)<extra></extra>',
        marker: {color: '#03045e'}
    };
    const tweets_bar6 = {
        x: twitter_hourly_time,
        y: twitter_hourly_data[1],
        name: '#BTC',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (#BTC)<extra></extra>',
        marker: {color: '#0077b6'}
    };
    const tweets_bar7 = {
        x: twitter_hourly_time,
        y: twitter_hourly_data[0],
        name: 'BTC',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (BTC)<extra></extra>',
        marker: {color: '#00b4d8'}
    };
    const tweets_bar8 = {
        x: twitter_hourly_time,
        y: twitter_hourly_data[2],
        name: 'Bitcoin',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (Bitcoin)<extra></extra>',
        marker: {color: '#90e0ef'}
    };
    const updatemenus = [{
        buttons: [{
            args: [{'visible': [false, false, false, false, true, true, true, true]},
                   {xaxis: {'tickformat': '%H:00', 'range': [twitter_hourly_time[47], twitter_hourly_time[0]]}}],
            label: '1H',
            method: 'update'
        },{
            args: [{'visible': [true, true, true, true, false, false, false, false]},
                   {xaxis: {'tickformat': '%b %d', 'range': [twitter_daily_time[twitter_daily_time.length-15],twitter_daily_time[twitter_daily_time.length-1]]}}],
            label: '1D',
            method: 'update'
        }],
        direction: 'left',
        pad: {'r': 0, 't': 0},
        showactive: true,
        type: 'buttons',
        x: 0,
        y: 1.2,
        xanchor: 'left',
        yanchor: 'top'
    }];
    const layout = {
        dragmode: 'pan',
        barmode: 'stack',
        title: 'Tweets count',
        autosize: false,
        height: 300,
        width: 600,
        updatemenus: updatemenus,
        margin: {r: 0, l: 35, b: 30, t: 30, pad: 5},
        legend: {
            "orientation": "h", x: 0.21, y: -0.15
        },
        yaxis: {
            fixedrange: true,
        },
        xaxis: {
            tickformat: '%H:00',
            range: [twitter_hourly_time[47], twitter_hourly_time[0]],
        },
    };
    Plotly.newPlot('twitter_div', [tweets_bar1, tweets_bar2, tweets_bar3, tweets_bar4, tweets_bar5, tweets_bar6, tweets_bar7, tweets_bar8], layout,{displayModeBar: false}, {responsive: true});
}
//{displayModeBar: false}, {responsive: true},

function RedditPlotCreate(){
    const tweets_bar1 = {
        visible: false,
        x: reddit_daily_time,
        y: reddit_daily_data[0],
        name: 'r/cryptocurrency',
        type: 'bar',
        connectgaps: true,
        hovertemplate: ' %{x},%{y} (r/cryptocurrency)<extra></extra>',
        marker: {color: '#FF5700'}
    };
    const tweets_bar2 = {
        visible: false,
        x: reddit_daily_time,
        y: reddit_daily_data[1],
        name: 'r/bitcoin',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (r/bitcoin)<extra></extra>',
        marker: {color: '#FFA500'}
    };
    const tweets_bar3 = {
        visible: false,
        x: reddit_daily_time,
        y: reddit_daily_data[2],
        name: 'r/btc',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (r/btc)<extra></extra>',
        marker: {color: '#FFCA00'}
    };
    const tweets_bar4 = {
        x: reddit_hourly_time,
        y: reddit_hourly_data[0],
        name: 'r/cryptocurrency',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (r/cryptocurrency)<extra></extra>',
        marker: {color: '#FF5700'}
    };
    const tweets_bar5 = {
        x: reddit_hourly_time,
        y: reddit_hourly_data[1],
        name: 'r/bitcoin',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (r/bitcoin)<extra></extra>',
        marker: {color: '#FFA500'}
    };
    const tweets_bar6 = {
        x: reddit_hourly_time,
        y: reddit_hourly_data[2],
        name: 'r/btc',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (r/btc)<extra></extra>',
        marker: {color: '#FFCA00'}
    };
    const updatemenus = [{
        buttons: [{
            args: [{'visible': [false, false, false, true, true, true]},
                   {xaxis: {'tickformat': '%H:00', 'range': [twitter_hourly_time[47], twitter_hourly_time[0]]}}],
            label: '1H',
            method: 'update'
        },{
            args: [{'visible': [true, true, true, false, false, false]},
                   {xaxis: {'tickformat': '%b %d', 'range': [twitter_daily_time[twitter_daily_time.length-15],twitter_daily_time[twitter_daily_time.length-1]]}}],
            label: '1D',
            method: 'update'
        }],
        direction: 'left',
        pad: {'r': 0, 't': 0},
        showactive: true,
        type: 'buttons',
        x: 0,
        y: 1.2,
        xanchor: 'left',
        yanchor: 'top'
    }];
    const layout = {
        dragmode: 'pan',
        barmode: 'stack',
        title: 'Reddit comments',
        autosize: false,
        height: 300,
        width: 600,
        updatemenus: updatemenus,
        margin: {r: 0, l: 35, b: 30, t: 30, pad: 5},
        legend: {
            "orientation": "h", x: 0.21, y: -0.15
        },
        yaxis: {
            fixedrange: true,
        },
        xaxis: {
            tickformat: '%H:00',
            range: [twitter_hourly_time[47], twitter_hourly_time[0]],
        },
    };
    Plotly.newPlot('reddit_div', [tweets_bar1, tweets_bar2, tweets_bar3, tweets_bar4, tweets_bar5, tweets_bar6], layout,{displayModeBar: false}, {responsive: true});
}

function GooglePlotCreate(){
    const tweets_bar1 = {
        visible: false,
        x: google_week_time,
        y: google_week_data[0],
        name: 'Search',
        type: 'bar',
        connectgaps: true,
        hovertemplate: ' %{x},%{y} (r/cryptocurrency)<extra></extra>',
        marker: {color: '#34A853'}
    };
    const tweets_bar2 = {
        visible: false,
        x: google_week_time,
        y: google_week_data[1],
        name: 'News',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (r/bitcoin)<extra></extra>',
        marker: {color: '#FBBC05'}
    };
    const tweets_bar3 = {
        visible: false,
        x: google_week_time,
        y: google_week_data[2],
        name: 'Youtube',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (r/btc)<extra></extra>',
        marker: {color: '#EA4335'}
    };
    const tweets_bar4 = {
        x: google_day_time,
        y: google_day_data[0],
        name: 'Search',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (r/cryptocurrency)<extra></extra>',
        marker: {color: '#34A853'}
    };
    const tweets_bar5 = {
        x: google_day_time,
        y: google_day_data[1],
        name: 'News',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (r/bitcoin)<extra></extra>',
        marker: {color: '#FBBC05'}
    };
    const tweets_bar6 = {
        x: google_day_time,
        y: google_day_data[2],
        name: 'Youtube',
        type: 'bar',
        hovertemplate: ' %{x},%{y} (r/btc)<extra></extra>',
        marker: {color: '#EA4335'}
    };
    const updatemenus = [{
        buttons: [{
            args: [{'visible': [false, false, false, true, true, true]}],
            label: 'Day',
            method: 'update'
        },{
            args: [{'visible': [true, true, true, false, false, false]}],
            label: 'Week',
            method: 'update'
        }],
        direction: 'left',
        pad: {'r': 0, 't': 0},
        showactive: true,
        type: 'buttons',
        x: 0,
        y: 1.2,
        xanchor: 'left',
        yanchor: 'top'
    }];
    const layout = {
        barmode: 'stack',
        bargap: 0.3,
        title: 'Google Trends',
        autosize: false,
        height: 300,
        width: 600,
        updatemenus: updatemenus,
        margin: {r: 0, l: 35, b: 30, t: 30, pad: 5},
        legend: {
            "orientation": "h", x: 0.21, y: -0.15
        },
        yaxis: {
            fixedrange: true,
        },
        xaxis: {
            fixedrange: true
        },
    };
    Plotly.newPlot('google2_div', [tweets_bar1, tweets_bar2, tweets_bar3, tweets_bar4, tweets_bar5, tweets_bar6], layout,{displayModeBar: false}, {responsive: true});
}
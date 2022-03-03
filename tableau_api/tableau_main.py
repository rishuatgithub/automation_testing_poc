import io

from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_views_dataframe, get_view_data_dataframe

TABLEAU_SERVER_CONFIG = {
    'my_env': {
        'server': 'https://public.tableau.com',
        'api_version': '3.0',
        'username': '',
        'password': '',
        # comment out username / password and uncomment the lines below to use personal access token authentication
        # 'personal_access_token_name': '<YOUR_PERSONAL_ACCESS_TOKEN_NAME>',
        # 'personal_access_token_secret': '<YOUR_PERSONAL_ACCESS_TOKEN_SECRET>',
        'site_name': '',
        'site_url': 'https://public.tableau.com/views/StrikeDashboard-2/StrikeDashboard'
    }
}

conn = TableauServerConnection(config_json=TABLEAU_SERVER_CONFIG, env='my_env')
conn.sign_in()

#views_df = get_views_dataframe(conn)
#print("views_df top rows:\n", views_df.head())
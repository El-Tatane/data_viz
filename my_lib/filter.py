# # filter target
# html.Div([
#     html.P("Objectif"),
#     dcc.Input(
#         id="input_num_subscribers",
#         type="number",
#         placeholder="input rating number",
#     ),
#     dcc.Input(
#         id="input_total_earn",
#         type="number",
#         placeholder="Gain total minimum",
#     ),
#     dcc.Dropdown(
#         id='drop_down_rating_number',
#         options=[{'label': i, 'value': i} for i in range(6)],
#         placeholder="Nombre d'étoile minimum",
#     )
#
# ]),
#
# # html.Div([
# #     dcc.Dropdown(
# #         id='drop_down_subject',
# #         options=[{'label': i, 'value': i} for i in data.get_unique_value("subject")],
# #         placeholder="input rating number",
# #     )
# # ])
# html.Div([
#     dcc.Graph(figure=get_radar_chart(data.get_radar_char()))
# ])
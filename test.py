import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="ReceptionData(May)",
                   page_icon=":bar_chart:",
                   layout="wide"
)

df=pd.read_excel(io='ReceptionData(May).xlsx',
                 engine='openpyxl',
                 sheet_name='Sheet1',
                 skiprows=0,
                 usecols='A:S',
                 nrows=1000,)
df['ManifestNumber_str'] = df['ManifestNumber'].astype(str)
df['inday_str'] = df['วันที่รับ'].astype(str)
df['outday_str'] = df['วันที่ออกผล'].astype(str)
df['company_str'] = df['บริษัท'].astype(str)
df['ทะเบียนรถ_str'] = df['ทะเบียนรถ'].astype(str)
df.drop("ManifestNumber",axis=1,inplace=True)
df.drop("วันที่รับ",axis=1,inplace=True)
df.drop("วันที่ออกผล",axis=1,inplace=True)
df.drop("บริษัท",axis=1,inplace=True)
df.drop("ทะเบียนรถ",axis=1,inplace=True)
df['Bulk Density_str'] = df['Bulk_Density'].astype(str)
df.drop("Bulk_Density",axis=1,inplace=True)
select='Sulfur'
select1='Wight'
df[select]=df[select].fillna(0)
df[select1]=df[select1].fillna(1)


st.sidebar.header("Please Filter Here: ")
inday_str=st.sidebar.multiselect(
    "Select the Inday",
    options=df["inday_str"].unique(),
    default=df["inday_str"].unique()
)

outday_str=st.sidebar.multiselect(
    "Select the outday",
    options=df["outday_str"].unique(),
    default=df["outday_str"].unique()
)

company_str=st.sidebar.multiselect(
    "Select the company",
    options=df["company_str"].unique(),
    default=df["company_str"].unique()
)

Waste_Name=st.sidebar.multiselect(
    "Select the Waste_Name",
    options=df["Waste_Name"].unique(),
    default=df["Waste_Name"].unique()
)

Type=st.sidebar.multiselect(
    "Select the Type",
    options=df["Type"].unique(),
    default=df["Type"].unique()
)

df_selection = df.query(
    "inday_str == @inday_str & outday_str == outday_str & company_str == company_str & Waste_Name == Waste_Name & Type == @Type")
st.title(":bar chart: Raw Data")
st.dataframe(df_selection)

df_Rawdata_inday=df.inday_str
df_Rawdata_ManifestNumber=df.ManifestNumber_str
df_Rawdata_company_str=df.company_str
df_Rawdata_Wight=df.Wight
df_Rawdata_Waste_Name=df.Waste_Name
df_Rawdata_Physical_characteristics=df.Physical_characteristics
df_Rawdata_LHV=df.LHV
df_Rawdata_Moisture=df.Moisture
df_Rawdata_Sulfur=df.Sulfur
df_Rawdata_Chloride=df.Chloride
df_Rawdata_data={'inday_str':df_Rawdata_inday,
                 'Wight':df_Rawdata_Wight,
       'ManifestNumber':df_Rawdata_ManifestNumber,
       'company_str':df_Rawdata_company_str,
       'Physical_characteristics':df_Rawdata_Physical_characteristics,
       'LHV':df_Rawdata_LHV,
       'Sulfur':df_Rawdata_Sulfur,
       'Chloride':df_Rawdata_Chloride,
       'Waste_Name':df_Rawdata_Waste_Name,
       'Moisture':df_Rawdata_Moisture,
       }
df_Rawdata=pd.DataFrame(df_Rawdata_data)

df_Rawdata_LHV_sum = df_Rawdata['LHV'].sum()
df_Rawdata_Moisture_sum = df_Rawdata['Moisture'].sum()
df_Rawdata_Sulfur_sum = df_Rawdata['Sulfur'].sum()
df_Rawdata_Chloride_sum = df_Rawdata['Chloride'].sum()
df_Rawdata_wight_sum = df_Rawdata['Wight'].sum()

df_Rawdata["LHV_Wight"]=df_Rawdata["LHV"]*df_Rawdata["Wight"]
df_Rawdata["Moisture_Wight"]=df_Rawdata["Moisture"]*df_Rawdata["Wight"]
df_Rawdata["Sulfur_Wight"]=df_Rawdata["Sulfur"]*df_Rawdata["Wight"]
df_Rawdata["Chloride_Wight"]=df_Rawdata["Chloride"]*df_Rawdata["Wight"]
df_Rawdata_LHV_Wight_sum = df_Rawdata['LHV_Wight'].sum()
df_Rawdata_Moisture_Wight_sum = df_Rawdata['Moisture_Wight'].sum()
df_Rawdata_Sulfur_Wight_sum = df_Rawdata['Sulfur_Wight'].sum()
df_Rawdata_Chloride_Wight_sum = df_Rawdata['Chloride_Wight'].sum()
df_Rawdata_LHV_meanwight=df_Rawdata_LHV_Wight_sum/df_Rawdata_wight_sum
df_Rawdata_Moisture_meanwight=df_Rawdata_Moisture_Wight_sum/df_Rawdata_wight_sum
df_Rawdata_Sulfur_meanwight=df_Rawdata_Sulfur_Wight_sum/df_Rawdata_wight_sum
df_Rawdata_Chloride_meanwight=df_Rawdata_Chloride_Wight_sum/df_Rawdata_wight_sum
column1,column2 =st.columns(2)
with column1:
    st.subheader("LHV_meanwight: ")
    st.subheader(f" {df_Rawdata_LHV_meanwight:,}")
with column2:
    st.subheader("Moisture_meanwight: ")
    st.subheader(f" {df_Rawdata_Moisture_meanwight:,}")

column3,column4 =st.columns(2)
with column3:
    st.subheader("Sulfur_meanwight: ")
    st.subheader(f" {df_Rawdata_Sulfur_meanwight:,}")
with column4:
    st.subheader("Chloride_meanwight: ")
    st.subheader(f" {df_Rawdata_Chloride_meanwight:,}")
    
std_LHV=int(df_selection["LHV"].std())
average_rating = round(df_selection["Chloride"].mean(),1)
star_rating = ":star:"*int(round(average_rating,0))
average_LHV_by_transection=round(df_selection["LHV"].mean(),2)
std_Moisture=int(df_selection["Moisture"].std())
std_Sulfur=round(df_selection["Sulfur"].std())
average_ratingMoisture = round(df_selection["Moisture"].mean(),1)
star_rating = ":star:"*int(round(average_rating,0))
average_Moisture_by_transection=round(df_selection["Moisture"].mean(),2)
std_Chloride=int(df_selection["Chloride"].std())
average_ratingChloride = round(df_selection["Chloride"].mean(),1)
star_rating = ":star:"*int(round(average_rating,0))
average_Chloride_by_transection=round(df_selection["Chloride"].mean(),2)

column1,column2,column3,column4 =st.columns(4)
with column1:
    st.subheader("LHV_std: ")
    st.subheader(f" {std_LHV:,}")
with column2:
    st.subheader("Moisture_std: ")
    st.subheader(f" {std_Moisture:,}")
with column3:
    st.subheader("Sulfur_std: ")
    st.subheader(f" {std_Sulfur:,}")
with column4:
    st.subheader("Chloride_std: ")
    st.subheader(f" {std_Chloride:,}")
    
fig_LHV_company_str = px.bar(
    df_Rawdata,
    x=df_selection["LHV"],
    y=df_selection["company_str"],
    orientation="h",
    title="<b>fig_LHV_ManifestNumber</b>",
    color_discrete_sequence=["#0083B8"] * len(df_Rawdata),
    template="plotly_white",
)
fig_LHV_company_str.update_xaxes(title_text='Low_Heating_(Kcal/kg)')
fig_LHV_company_str.update_yaxes(title_text='บริษัท')

fig_LHV_company_str.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

fig_Moisture_company_str= px.bar(
    df_Rawdata,
    x=df_selection["Moisture"],
    y=df_selection["company_str"],
    orientation="h",
    title="<b>fig_Moisture_ManifestNumber</b>",
    color_discrete_sequence=["#0083B8"] * len(df_Rawdata),
    template="plotly_white",
)
fig_Moisture_company_str.update_xaxes(title_text='%Moisture')
fig_Moisture_company_str.update_yaxes(title_text='บริษัท')

fig_Moisture_company_str.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_LHV_company_str, use_container_width=True)
right_column.plotly_chart(fig_Moisture_company_str, use_container_width=True)

fig_Chloride_company_str = px.bar(
    df_Rawdata,
    x=df_selection["Chloride"],
    y=df_selection["company_str"],
    orientation="h",
    title="<b>fig_Chloride_ManifestNumber</b>",
    color_discrete_sequence=["#0083B8"] * len(df_Rawdata),
    template="plotly_white",
)
fig_Chloride_company_str.update_xaxes(title_text='%Chloride')
fig_Chloride_company_str.update_yaxes(title_text='บริษัท')

fig_Chloride_company_str.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

fig_Sulfur_company_str= px.bar(
    df_Rawdata,
    x=df_selection["Sulfur"],
    y=df_selection["company_str"],
    orientation="h",
    title="<b>fig_Sulfur_Xray_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(df_Rawdata),
    template="plotly_white",
)
fig_Sulfur_company_str.update_xaxes(title_text='%Sulfur')
fig_Sulfur_company_str.update_yaxes(title_text='บริษัท')

fig_Sulfur_company_str.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_Chloride_company_str, use_container_width=True)
right_column.plotly_chart(fig_Sulfur_company_str, use_container_width=True)

st.title(":bar chart: Reception Analysis")
st.markdown('##')

std_LHV=int(df_selection["LHV"].std())
average_rating = round(df_selection["Chloride"].mean(),1)
star_rating = ":star:"*int(round(average_rating,0))
average_LHV_by_transection=round(df_selection["LHV"].mean(),2)

left_column,middle_column,right_column =st.columns(3)
with left_column:
    st.subheader("std LHV: ")
    st.subheader(f"c {std_LHV:,}")
with middle_column:
    st.subheader("Average Rating: ")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average LHV Per Transaction: ")
    st.subheader(f"c {average_LHV_by_transection}")

st.markdown("---")
st.markdown('##')

std_Moisture=int(df_selection["Moisture"].std())
std_Sulfur=round(df_selection["Sulfur"].std())
average_ratingMoisture = round(df_selection["Moisture"].mean(),1)
star_rating = ":star:"*int(round(average_rating,0))
average_Moisture_by_transection=round(df_selection["Moisture"].mean(),2)

left_column,middle_column,right_column =st.columns(3)
with left_column:
    st.subheader("std Moisture: ")
    st.subheader(f"% {std_Moisture:,}")
with middle_column:
    st.subheader("std_Sulfur: ")
    st.subheader(f"{std_Sulfur:,} ")
with right_column:
    st.subheader("Average Moisture Per Transaction: ")
    st.subheader(f"% {average_Moisture_by_transection}")

st.markdown("---")
st.markdown('##')

std_Chloride=int(df_selection["Chloride"].std())
average_ratingChloride = round(df_selection["Chloride"].mean(),1)
star_rating = ":star:"*int(round(average_rating,0))
average_Chloride_by_transection=round(df_selection["Chloride"].mean(),2)

left_column,middle_column,right_column =st.columns(3)
with left_column:
    st.subheader("std Chloride: ")
    st.subheader(f"% {std_Chloride:,}")
with middle_column:
    st.subheader("Average Rating: ")
    st.subheader(f"{average_ratingChloride} {star_rating}")
with right_column:
    st.subheader("Average Chloride Per Transaction: ")
    st.subheader(f"% {average_Chloride_by_transection}")

st.markdown("---")



non_HZ=df[df.Type == "Non-Hz"]
non_HZ_inday=non_HZ.inday_str
non_HZ_company_str=non_HZ.company_str
non_HZ_Type=non_HZ.Type
non_HZ_ManifestNumber=non_HZ.ManifestNumber_str
non_HZ_Waste_Name=non_HZ.Waste_Name
non_HZ_Physical_characteristics=non_HZ.Physical_characteristics
non_HZ_LHV=non_HZ.LHV
non_HZ_Sulfur=non_HZ.Sulfur
non_HZ_Chloride=non_HZ.Chloride
non_HZ_Moisture=non_HZ.Moisture
non_HZ_data={'inday_str':non_HZ_inday,
             'Chloride':non_HZ_Chloride,
             'Sulfur':non_HZ_Sulfur,
             'Type':non_HZ_Type,
       'ManifestNumber':non_HZ_ManifestNumber,
       'company_str':non_HZ_company_str,
       'Physical_characteristics':non_HZ_Physical_characteristics,
       'LHV':non_HZ_LHV,
       'Waste_Name':non_HZ_Waste_Name,
       'Moisture':non_HZ_Moisture,
       }
non_HZ_df=pd.DataFrame(non_HZ_data)



NonHZ_selection = non_HZ_df.query("inday_str == @inday_str & Type == @Type")
st.title(":bar chart: Non-HZ")
st.dataframe(NonHZ_selection)

fig_LHV_company_str_non = px.bar(
    non_HZ_df,
    x=NonHZ_selection["LHV"],
    y=NonHZ_selection["company_str"],
    orientation="h",
    title="<b>fig_LHV_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(non_HZ_df),
    template="plotly_white",
)
fig_LHV_company_str_non.update_xaxes(title_text='Low_Heating_(Kcal/kg)')
fig_LHV_company_str_non.update_yaxes(title_text='บริษัท')
fig_LHV_company_str_non.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

fig_Moisture_company_str_non= px.bar(
    non_HZ_df,
    x=NonHZ_selection["Moisture"],
    y=NonHZ_selection["company_str"],
    orientation="h",
    title="<b>fig_Moisture_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(non_HZ_df),
    template="plotly_white",
)
fig_Moisture_company_str_non.update_xaxes(title_text='%Moisture')
fig_Moisture_company_str_non.update_yaxes(title_text='บริษัท')

fig_Moisture_company_str_non.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

non_HZ_df_good=non_HZ_df.loc[(non_HZ_df.LHV >3000) | (non_HZ_df.Moisture<30) | (non_HZ_df.Chloride<6) | (non_HZ_df.Sulfur<10)]
non_HZ_df_bad=non_HZ_df.loc[(non_HZ_df.LHV <3000) | (non_HZ_df.Moisture>30) | (non_HZ_df.Chloride>6) | (non_HZ_df.Sulfur>10)]

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_LHV_company_str_non, use_container_width=True)
right_column.plotly_chart(fig_Moisture_company_str_non, use_container_width=True)

fig_Chloride_company_str_non = px.bar(
    non_HZ_df,
    x=NonHZ_selection["Chloride"],
    y=NonHZ_selection["company_str"],
    orientation="h",
    title="<b>fig_Chloride_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(non_HZ_df),
    template="plotly_white",
)
fig_Chloride_company_str_non.update_xaxes(title_text='%Chloride')
fig_Chloride_company_str_non.update_yaxes(title_text='บริษัท')

fig_Chloride_company_str_non.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

fig_Sulfur_company_str_non= px.bar(
    non_HZ_df,
    x=NonHZ_selection["Sulfur"],
    y=NonHZ_selection["company_str"],
    orientation="h",
    title="<b>fig_Sulfur_Xray_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(non_HZ_df),
    template="plotly_white",
)
fig_Sulfur_company_str_non.update_xaxes(title_text='%Sulfur')
fig_Sulfur_company_str.update_yaxes(title_text='บริษัท')

fig_Sulfur_company_str_non.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_Chloride_company_str_non, use_container_width=True)
right_column.plotly_chart(fig_Sulfur_company_str_non, use_container_width=True)

st.markdown('##')
NonHZ_selection_good= non_HZ_df_good.query("inday_str == @inday_str & Type == @Type")
NonHZ_selection_bad= non_HZ_df_bad.query("inday_str == @inday_str & Type == @Type")
left_column,middle_column =st.columns(2)
with left_column:
    st.title(":bar chart: Non-HZ-Good")
    st.dataframe(NonHZ_selection_good)
with middle_column:
    st.title(":bar chart: Non-HZ-Bad")
    st.dataframe(NonHZ_selection_bad)
st.markdown('--')
NonHZ_selection_good= non_HZ_df.query("inday_str == @inday_str & Type == @Type")


HZ=df[df.Type == "Hz"]
HZ_inday=HZ.inday_str
HZ_Type=HZ.Type
HZ_company_str=HZ.company_str
HZ_ManifestNumber=HZ.ManifestNumber_str
HZ_Waste_Name=HZ.Waste_Name
HZ_Physical_characteristics=HZ.Physical_characteristics
HZ_LHV=HZ.LHV
HZ_Sulfur=HZ.Sulfur
HZ_Chloride=HZ.Chloride
HZ_Moisture=HZ.Moisture
HZ_data={'inday_str':HZ_inday,
         'Type':HZ_Type,
         'Chloride':HZ_Chloride,
         'Sulfur':HZ_Sulfur,
         'company_str':HZ_company_str,
       'ManifestNumber':HZ_ManifestNumber,
       'Physical_characteristics':HZ_Physical_characteristics,
       'LHV':HZ_LHV,
       'Waste_Name':HZ_Waste_Name,
       'Moisture':HZ_Moisture,
       }
HZ_df=pd.DataFrame(HZ_data)
HZ_selection = HZ_df.query("inday_str == @inday_str & Type == @Type")
HZ_df_good=HZ_df.loc[(HZ_df.LHV >3000) | (HZ_df.Moisture<30) | (HZ_df.Chloride<6) | (HZ_df.Sulfur<10)]
HZ_df_bad=HZ_df.loc[(HZ_df.LHV <3000) | (HZ_df.Moisture>30) | (HZ_df.Chloride>=6) | (HZ_df.Sulfur>10)]
HZ_selection_good= HZ_df_good.query("inday_str == @inday_str & Type == @Type")
HZ_selection_bad= HZ_df_bad.query("inday_str == @inday_str & Type == @Type")
st.title(":bar chart: HZ")
st.dataframe(HZ_selection)

fig_LHV_company_str_HZ = px.bar(
    HZ_df,
    x=HZ_selection["LHV"],
    y=HZ_selection["company_str"],
    orientation="h",
    title="<b>fig_LHV_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(HZ_df),
    template="plotly_white",
)
fig_LHV_company_str_HZ.update_xaxes(title_text='Low_Heating_(Kcal/kg)')
fig_LHV_company_str_HZ.update_yaxes(title_text='บริษัท')

fig_LHV_company_str_HZ.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

fig_Moisture_company_str_HZ= px.bar(
    non_HZ_df,
    x=HZ_selection["Moisture"],
    y=HZ_selection["company_str"],
    orientation="h",
    title="<b>fig_Moisture_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(HZ_df),
    template="plotly_white",
)
fig_Moisture_company_str_HZ.update_xaxes(title_text='%Moisture')
fig_Moisture_company_str_HZ.update_yaxes(title_text='บริษัท')

fig_Moisture_company_str_HZ.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_LHV_company_str_HZ, use_container_width=True)
right_column.plotly_chart(fig_Moisture_company_str_HZ, use_container_width=True)

fig_Chloride_company_str_HZ = px.bar(
    HZ_df,
    x=HZ_selection["Chloride"],
    y=HZ_selection["company_str"],
    orientation="h",
    title="<b>fig_Chloride_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(HZ_df),
    template="plotly_white",
)
fig_Moisture_company_str_HZ.update_xaxes(title_text='%Chloride')
fig_Moisture_company_str_HZ.update_yaxes(title_text='บริษัท')

fig_Chloride_company_str_HZ.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

fig_Sulfur_company_str_HZ= px.bar(
    HZ_df,
    x=HZ_selection["Sulfur"],
    y=HZ_selection["company_str"],
    orientation="h",
    title="<b>fig_Sulfur_Xray_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(HZ_df),
    template="plotly_white",
)
fig_Moisture_company_str_HZ.update_xaxes(title_text='%Sulfur')
fig_Moisture_company_str_HZ.update_yaxes(title_text='บริษัท')

fig_Sulfur_company_str_HZ.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_Chloride_company_str_HZ, use_container_width=True)
right_column.plotly_chart(fig_Sulfur_company_str_HZ, use_container_width=True)

st.markdown('##')
left_column,middle_column =st.columns(2)
with left_column:
    st.title(":bar chart: HZ-Good")
    st.dataframe(HZ_selection_good)
with middle_column:
    st.title(":bar chart: HZ-Bad")
    st.dataframe(HZ_selection_bad)
st.markdown('--')

Oil_Sludge=df[df.Type == "Oil Sludge"]
Oil_Sludge_inday=Oil_Sludge.inday_str
Oil_Sludge_Type=Oil_Sludge.Type
Oil_Sludge_company_str=Oil_Sludge.company_str
Oil_Sludge_ManifestNumber=Oil_Sludge.ManifestNumber_str
Oil_Sludge_Waste_Name=Oil_Sludge.Waste_Name
Oil_Sludge_Physical_characteristics=Oil_Sludge.Physical_characteristics
Oil_Sludge_LHV=Oil_Sludge.LHV
Oil_Sludge_Sulfur=Oil_Sludge.Sulfur
Oil_Sludge_Chloride=Oil_Sludge.Chloride
Oil_Sludge_Moisture=Oil_Sludge.Moisture
Oil_Sludge_data={'inday_str':Oil_Sludge_inday,
                 'Type':Oil_Sludge_Type,
                 'Chloride':Oil_Sludge_Chloride,
                 'Sulfur':Oil_Sludge_Sulfur,
                 'company_str':Oil_Sludge_company_str,
       'ManifestNumber':Oil_Sludge_ManifestNumber,
       'Physical_characteristics':Oil_Sludge_Physical_characteristics,
       'LHV':Oil_Sludge_LHV,
       'Waste_Name':Oil_Sludge_Waste_Name,
       'Moisture':Oil_Sludge_Moisture,
       }
Oil_Sludge_df=pd.DataFrame(Oil_Sludge_data)
Oil_Sludge_selection = Oil_Sludge_df.query("inday_str == @inday_str & Type == @Type")
Oil_Sludge_df_good=Oil_Sludge_df.loc[(Oil_Sludge_df.LHV >2000) | (Oil_Sludge_df.Moisture<40) | (Oil_Sludge_df.Sulfur<15) | (Oil_Sludge_df.Chloride<6)]
Oil_Sludge_df_bad=Oil_Sludge_df.loc[(Oil_Sludge_df.LHV <2000) | (Oil_Sludge_df.Moisture>40) | (Oil_Sludge_df.Sulfur>15) | (Oil_Sludge_df.Chloride<6)]
st.title(":bar chart: Oil_Sludge")
Oil_Sludge_selection_good= Oil_Sludge_df_good.query("inday_str == @inday_str & Type == @Type")
Oil_Sludge_selection_bad= Oil_Sludge_df_bad.query("inday_str == @inday_str & Type == @Type")
st.dataframe(Oil_Sludge_selection)

fig_LHV_ManifestNumber_Oil_Sludge = px.bar(
    Oil_Sludge_df,
    x=Oil_Sludge_selection["LHV"],
    y=Oil_Sludge_selection["company_str"],
    orientation="h",
    title="<b>fig_LHV_ManifestNumber</b>",
    color_discrete_sequence=["#0083B8"] * len(Oil_Sludge_df),
    template="plotly_white",
)

fig_LHV_ManifestNumber_Oil_Sludge.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

fig_Moisture_ManifestNumber_Oil_Sludge= px.bar(
    Oil_Sludge_df,
    x=Oil_Sludge_selection["Moisture"],
    y=Oil_Sludge_selection["company_str"],
    orientation="h",
    title="<b>fig_Moisture_ManifestNumber</b>",
    color_discrete_sequence=["#0083B8"] * len(Oil_Sludge_df),
    template="plotly_white",
)

fig_Moisture_ManifestNumber_Oil_Sludge.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_LHV_ManifestNumber_Oil_Sludge, use_container_width=True)
right_column.plotly_chart(fig_Moisture_ManifestNumber_Oil_Sludge, use_container_width=True)

fig_Chloride_company_str = px.bar(
    Oil_Sludge_df,
    x=Oil_Sludge_selection["Chloride"],
    y=Oil_Sludge_selection["company_str"],
    orientation="h",
    title="<b>fig_Chloride_ManifestNumber</b>",
    color_discrete_sequence=["#0083B8"] * len(Oil_Sludge_df),
    template="plotly_white",
)

fig_Chloride_company_str.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

fig_Sulfur_company_str= px.bar(
    Oil_Sludge_df,
    x=Oil_Sludge_selection["Sulfur"],
    y=Oil_Sludge_selection["company_str"],
    orientation="h",
    title="<b>fig_Sulfur_Xray_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(Oil_Sludge_df),
    template="plotly_white",
)

fig_Sulfur_company_str.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_Chloride_company_str, use_container_width=True)
right_column.plotly_chart(fig_Sulfur_company_str, use_container_width=True)

st.markdown('##')
left_column,middle_column =st.columns(2)
with left_column:
    st.title(":bar chart: Oil_Sludge-Good")
    st.dataframe(Oil_Sludge_selection_good)
    # print(Oil_Sludge_selection_good)
with middle_column:
    st.title(":bar chart: Oil_Sludge-Bad")
    st.dataframe(Oil_Sludge_selection_bad)
    # print(Oil_Sludge_df_bad)
st.markdown('--')

Product=df[df.Type == "Product"]
Product_inday=Product.inday_str
Product_Type=Product.Type
Product_company_str=Product.company_str
Product_ManifestNumber=Product.ManifestNumber_str
Product_Waste_Name=Product.Waste_Name
Product_Physical_characteristics=Product.Physical_characteristics
Product_LHV=Product.LHV
Product_Sulfur=Product.Sulfur
Product_Chloride=Product.Chloride
Product_Moisture=Product.Moisture
Product_data={'inday_str':Product_inday,
              'Type':Product_Type,
              'Chloride':Product_Chloride,
              'Sulfur':Product_Sulfur,
              'company_str':Product_company_str,
       'ManifestNumber':Product_ManifestNumber,
       'Physical_characteristics':Product_Physical_characteristics,
       'LHV':Product_LHV,
       'Waste_Name':Product_Waste_Name,
       'Moisture':Product_Moisture,
       }
Product_df=pd.DataFrame(Product_data)
Product_selection = Product_df.query("inday_str == @inday_str & Type == @Type")
Product_df_good=Product_df.loc[(Product_df.LHV >3500) | (Product_df.Moisture<35) | (Product_df.Chloride<6) | (Product_df.Sulfur<15)]
Product_df_bad=Product_df.loc[(Product_df.LHV <3500) | (Product_df.Moisture>35) | (Product_df.Chloride>6) | (Product_df.Sulfur>15)]
st.title(":bar chart: Product")
st.dataframe(Product_selection)


fig_LHV_ManifestNumber_Product = px.bar(
    Product_df,
    x=Product_selection["LHV"],
    y=Product_selection["company_str"],
    orientation="h",
    title="<b>fig_LHV_ManifestNumber</b>",
    color_discrete_sequence=["#0083B8"] * len(Product_df),
    template="plotly_white",
)

fig_LHV_ManifestNumber_Product.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

fig_Moisture_ManifestNumber_Product= px.bar(
    Product_df,
    x=Product_selection["Moisture"],
    y=Product_selection["company_str"],
    orientation="h",
    title="<b>fig_Moisture_ManifestNumber</b>",
    color_discrete_sequence=["#0083B8"] * len(Product_df),
    template="plotly_white",
)

fig_Moisture_ManifestNumber_Product.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_LHV_ManifestNumber_Product, use_container_width=True)
right_column.plotly_chart(fig_Moisture_ManifestNumber_Product, use_container_width=True)

fig_Chloride_company_str = px.bar(
    Product_df,
    x=Product_selection["Chloride"],
    y=Product_selection["company_str"],
    orientation="h",
    title="<b>fig_Chloride_ManifestNumber</b>",
    color_discrete_sequence=["#0083B8"] * len(Oil_Sludge_df),
    template="plotly_white",
)

fig_Chloride_company_str.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

fig_Sulfur_Xray_company_str= px.bar(
    Product_df,
    x=Product_selection["Sulfur"],
    y=Product_selection["company_str"],
    orientation="h",
    title="<b>fig_Sulfur_Xray_company_str</b>",
    color_discrete_sequence=["#0083B8"] * len(Oil_Sludge_df),
    template="plotly_white",
)

fig_Sulfur_company_str.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_Chloride_company_str, use_container_width=True)
right_column.plotly_chart(fig_Sulfur_Xray_company_str, use_container_width=True)

Product_selection_good= Product_df_good.query("inday_str == @inday_str & Type == @Type")
Product_selection_bad= Product_df_bad.query("inday_str == @inday_str & Type == @Type")


st.markdown('##')
left_column,middle_column =st.columns(2)
with left_column:
    st.title(":bar chart: Product-Good")
    st.dataframe(Product_selection_good)
with middle_column:
    st.title(":bar chart: Product-Bad")
    st.dataframe(Product_selection_bad)
st.markdown('--')

nan=df[df.Type == "nan"]
nan_inday=nan.inday_str
nan_Type=nan.Type
nan_ManifestNumber=nan.ManifestNumber_str
nan_company_str=nan.company_str
nan_Waste_Name=nan.Waste_Name
nan_Physical_characteristics=nan.Physical_characteristics
nan_LHV=nan.LHV
nan_Moisture=nan.Moisture
nan_data={'inday':nan_inday,
          'Type':nan_Type,
          'company_str':nan_company_str,
       'ManifestNumbe':nan_ManifestNumber,
       'Physical_characteristics':nan_Physical_characteristics,
       'LHV':nan_LHV,
       'Waste_Name':nan_Waste_Name,
       'Moisture':nan_Moisture,
       }
nan_df=pd.DataFrame(nan_data)
nan_df_good=nan_df.loc[(nan_df.LHV >3000) | (nan_df.Moisture<30)]
nan_df_bad=nan_df.loc[(Product_df.LHV <3000) | (nan_df.Moisture>30)]
st.title(":bar chart: nan")
st.dataframe(nan_df)
st.markdown('##')
left_column,middle_column =st.columns(2)
with left_column:
    st.title(":bar chart: nan-Good")
    st.dataframe(nan_df_good)
with middle_column:
    st.title(":bar chart: nan-Bad")
    st.dataframe(nan_df_bad)
st.markdown('--')




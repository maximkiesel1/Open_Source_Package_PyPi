# PackagePyPi: Tool For NaN-Value Analyzation and Viusalization

## Installation

The package can be installed using pip:

pip install NaN_Rate_Calc_Vis

## Usage

To use the NaN_Rate_Calc_Vis class, you need to import the class and initialize it with a Dataframe.

import NaN_Rate_Calc_Vis as nc

df = pd.read_csv("data.csv")
nc_vis = nc.NaN_Rate_Calc_Vis(df)

Calculate the NaN-Quote of the whole dataframe

To calculate the NaN-Quote of the whole dataframe, use the method nan_quote_df

nc_vis.nan_quote_df()

This method returns a dictionary with the columns as keys and the corresponding NaN-rate.
Plot the bar chart of the NaN rate for all columns of the dataset

To plot the bar chart of the NaN rate for all columns of the dataset, use the method barchart_columns. Make sure to call the nan_quote_df method first.

nc_vis.barchart_columns(fig_lenght, fig_wide)

The fig_lenght and fig_wide parameters define the size of the plotted figure.
Create a dictonary that shows the nan quote of one column related to the other column

To create a dictonary that shows the nan quote of one column related to the other column, use the method infl_nan_columns.

nc_vis.infl_nan_columns(column, na_column)

This method takes two parameters:

    column: the target column to check the influence
    na_column: the column with their nan rates

It returns a dictionary with the unique values of a column as keys and the nan rates of the corresponding na_column.
Plot the barchart of the NaN rate for all columns of the dataset

To plot the barchart of the NaN rate for all columns of the dataset, use the method barchart_infl_nan_columns. Make sure to call the infl_nan_columns method first.

nc_vis.barchart_infl_nan_columns(fig_lenght, fig_wide)

The fig_lenght and fig_wide parameters define the size of the plotted figure.
Example
```
import NaN_Rate_Calc_Vis as nc
import pandas as pd

df = pd.read_csv("data.csv")
nc_vis = nc.NaN_Rate_Calc_Vis(df)

nc_vis.nan_quote_df()
nc_vis.barchart_columns(10, 5)
nc_vis.infl_nan_columns("column1", "column2")
nc_vis.barchart_infl_nan_columns(10, 5)
```
## License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Hat tip to anyone whose code was used
Inspiration
etc

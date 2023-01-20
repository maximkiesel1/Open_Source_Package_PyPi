import unittest
from Barchart_Visual import plot_barchart

class TestBarchart_Visual(unittest.Barchart_Visual):
    """
    This class contains unit tests for the Barchart_Visual class.
    """

    def test_plot_created(self):
        """
        Tests whether a barchart plot is created when the plot_barchart() 
        method is called.
        """
        # Create an instance of Barchart_Visual
        obj = Barchart_Visual()
        # Call the plot_barchart() method
        obj.plot_barchart()
        # Check if a plot was created
        self.assertTrue(len(plt.get_fignums()) > 0)

if __name__ == '__main__':
    unittest.main()
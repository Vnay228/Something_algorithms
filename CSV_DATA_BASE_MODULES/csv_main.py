import csv
import sys
import os

import pandas


from pprint import pprint


class CSVdatabase:
	"""docstring for DataDas"""

	def __init__( self, csv_table_name : str ):
		self.__CSVdatabase_dir_name = self.__get_file_dir_name(); 
		self.__CSVdatabase_name = self.__CSVdatabase_dir_name + "\\" + csv_table_name
		try:
			self.__CSVdatabase_lenght = len( pandas.read_csv( self.__CSVdatabase_name ).index ) if  os.path.isfile(self.__CSVdatabase_name) else 0		
			if self.__CSVdatabase_lenght != 0:
				

		except pandas.errors.EmptyDataError:
			self.__CSVdatabase_lenght = 0
		self.__CSVdatabase_keys = []
		self.__CSVdatabase_infor_type = 1;


	def dump_into_csv( self, parameters : dict, rewrite : bool = True ):
		''''''
		self.__CSVdatabase_infor_type == 1
		self.__init_single_values( parameters );


	def dumps_into_csv( self, parameters : list, rewrite : bool = True  ):
		''''''
		self.__CSVdatabase_infor_type == 2
		self.__init_significant_values( parameters );


	def write( self, flag : str="all", indexs: list=[0], index : int=None ):
		''''''
		if index == None:
			index = self.__CSVdatabase_lenght
		
		if flag == "all":
			self.__write_all()
		elif flag == "single":
			self.__write_single( index )
		elif flag == "selective":
			self.__write_selective( indexs )


	''' --------------- magics method Overriding -------------- '''

	def __iter__( self ):
		for variable_key in self.__CSVdatabase_keys:
			yield variable_key, getattr( self, variable_key )


	''' --------------- private methods ----------------------- '''

	''' write method '''
	def __write_all( self ):
		data = dict( self )
		index=[ i for i in range( self.__CSVdatabase_lenght, self.__CSVdatabase_lenght+ len( getattr( self, list( self.__CSVdatabase_keys )[0] ) ) ) ]		
		df = pandas.DataFrame( data, columns=list( self.__CSVdatabase_keys ), index=index)
		df.to_csv( self.__CSVdatabase_name, mode='a', header=False if self.__CSVdatabase_lenght != 0 else True )
		self.__CSVdatabase_lenght+=len( getattr( self, list( self.__CSVdatabase_keys )[0] ) )


	def __write_single( self, index : int ):
		if self.__CSVdatabase_lenght == index:
			self.__write_single_in_the_last_position( index )
		
		else:
			self.__write_single_in_the_midle_position( index )


	def __write_single_in_the_midle_position( self, index : int  ):
		left_df = self.__write_single_get_left_dataframe( index )
		right_df = self.__write_single_get_right_dataframe( index )
		pprint(left_df)
		pprint(right_df)



	def __write_single_get_right_dataframe( self, index : int ):
		indexs = [ i for i in range( index, self.__CSVdatabase_lenght ) ]
		return pandas.read_csv( self.__CSVdatabase_name ).loc[[indexs]]


	def __write_single_get_left_dataframe( self, index : int ):
		indexs = [ i for i in range( 0, index ) ]
		return pandas.read_csv( self.__CSVdatabase_name ).loc[[indexs]]


	def __write_single_in_the_last_position( self, index : int ):
		df = pandas.DataFrame( dict(self), columns=list( self.__CSVdatabase_keys ), index=[self.__CSVdatabase_lenght])
		df.to_csv( self.__CSVdatabase_name, mode='a', header=False if self.__CSVdatabase_lenght != 0 else True )
		self.__CSVdatabase_lenght+=1;


	def __write_selective( self ):
		pass

	''' sys method '''
	def __get_file_dir_name( self ):
		path = os.path.abspath(__file__)
		return os.path.dirname( path )


	''' init methods'''
	def __init_single_values( self, parameters : dict ):
		self.__CSVdatabase_keys = parameters.keys();
		if type( parameters ) == dict:
			for param_tail,param_value in parameters.items():
				setattr( self, param_tail, param_value )



	def __init_significant_values( self, parameters : list ):
		self.__CSVdatabase_keys = parameters[0].keys();
		if type( parameters ) == list:
			for key in self.__CSVdatabase_keys:
				setattr( self, key, [ parameter[ key ] for parameter in parameters ] );



if __name__ == '__main__':
	case1 = {
		"name": "afasfas",
		"passpword": "asfafaf",
		"item": 12,
		"birthday" : "2000",
		"infor" : "afasfafaafsafafsafsafsfasasfafsafsafs"
	}
	case2 = {
		"name": "afasfas",
		"passpword": "asfafaf",
		"item": 12,
		"birthday" : "2000",
		"infor" : "afasfafaafsafafsafsafsfasasfafsafsafs"
	}

	with open('test.txt', 'a+', encoding='utf8') as csv_file:
		pass

	DataBase1 = CSVdatabase("test1.csv")
	DataBase2 = CSVdatabase("test2.csv")


	DataBase1.dump_into_csv(case1);
	pprint(dict(DataBase1))
	# DataBase1.write()


	DataBase2.dumps_into_csv([case1, case2]);
	pprint(dict(DataBase2))
	DataBase2.write(flag = "single", index=1)


import pandas as pd
import random


class Foreign_Keys:
      def __init__(self, df, db_fk_field_name, foreign_key_abbreviation_pre = "", foreign_key_abbreviation_post = ""):
            self.df = df
            self.db_fk_field_name = db_fk_field_name
            self.foreign_key_abbreviation_pre = foreign_key_abbreviation_pre
            self.foreign_key_abbreviation_post = foreign_key_abbreviation_post
      
      def add_foreignkey_random(self, df2, col_placement = 3):
            if self.db_fk_field_name not in self.df.columns:
                  raise ValueError(f"{self.db_fk_field_name} not in first DataFrame")
            
            db_fk_list = self.df[self.db_fk_field_name].tolist()
            random_fk_values = [random.choice(db_fk_list) for _ in range(len(df2))]
            
            if self.db_fk_field_name in df2.columns:
                  df2 = df2.drop(columns=self.db_fk_field_name)
            
            df2.insert(col_placement - 1, self.foreign_key_abbreviation_pre + self.db_fk_field_name + self.foreign_key_abbreviation_post, random_fk_values)
            return df2
            
      
      def add_foreignkey_conditions(self):
            pass
      

class Intermediary_Data:
      def __init__(self, relationship_id_field_name = "Relationship ID"):
            self.rel_id_name = relationship_id_field_name
      
      # Two databases establishing a data relationship where the db1 IDs - db2 IDs are randomized 
      def create_2db_relationship_df_random(self, df1, df1_id_field_name, df2, df2_id_field_name):
            new_relationship_df = pd.DataFrame()
            new_relationship_df[df1_id_field_name] = df1[df1_id_field_name]
            
            random_rel_id = random.sample(range(1, len(df1) + 1), len(df1))
            new_relationship_df.insert(0, self.rel_id_name, random_rel_id)
            
            random_df2_id_list = [random.choice(df2[df2_id_field_name]) for _ in range(len(df1))]
            new_relationship_df[df2_id_field_name] = random_df2_id_list
            
            return new_relationship_df
            
      
      # Three databases establishing a data relationship where the db1 IDs - db2 IDs - db3 IDs are randomized 
      def create_3db_relationship_df_random(self, df1, df1_id_field_name, df2, df2_id_field_name, df3, df3_id_field_name):
            new_relationship_df = pd.DataFrame()
            new_relationship_df[df1_id_field_name] = df1[df1_id_field_name]
            
            random_rel_id = [random.randint(1,len(df1)) for _ in range(len(df1))]
            new_relationship_df.insert(0, self.rel_id_name, random_rel_id)
            
            random_df2_id_list = [random.choice(df2[df2_id_field_name]) for _ in range(len(df1))]
            new_relationship_df[df2_id_field_name] = random_df2_id_list
            
            random_df3_id_list = [random.choice(df3[df3_id_field_name]) for _ in range(len(df1))]
            new_relationship_df[df3_id_field_name] = random_df3_id_list
            
            return new_relationship_df
      
      # Two databases establishing a data relationship with a trait category where the db1 IDs - db2 IDs are randomized 
      def create_2db_relationship_df_random_trait(self, df1, df1_id_field_name, df2, df2_id_field_name, trait):
            new_relationship_df = pd.DataFrame()
            new_relationship_df[df1_id_field_name] = df1[df1_id_field_name]
            
            random_rel_id = random.sample(range(1, len(df1) + 1), len(df1))
            new_relationship_df.insert(0, self.rel_id_name, random_rel_id)
            
            random_df2_id_list = [random.choice(df2[df2_id_field_name]) for _ in range(len(df1))]
            new_relationship_df[df2_id_field_name] = random_df2_id_list
            
            random_trait_list = [random.choice(trait) for _ in range(len(df1))]
            new_relationship_df['Relationship Trait'] = random_trait_list
            
            return new_relationship_df
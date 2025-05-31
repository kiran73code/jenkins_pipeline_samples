from simple_python.utils.data_frames import (
    create_fancy_dataframe,
    print_dataframe_info
)

def main():
    print(" simple-python-script!")
    fancy_df = create_fancy_dataframe()
    print_dataframe_info(fancy_df)  
    print("Done!")


if __name__ == "__main__":
    main()

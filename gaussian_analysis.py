import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    correct_type_loc = (isinstance(loc, int) or isinstance(loc, float))
    correct_type_scale = (isinstance(scale, int) or isinstance(scale, float))
    correct_type_lower_bound = (isinstance(lower_bound, int) or isinstance(lower_bound, float))
    correct_type_upper_bound = (isinstance(upper_bound, int) or isinstance(upper_bound, float))
    if (correct_type_loc and correct_type_scale and correct_type_lower_bound and correct_type_upper_bound):
        if (lower_bound < upper_bound):
            samples = np.random.normal(loc, scale, 100)
            samples = [x for x in samples if (x > lower_bound and x < upper_bound)]
            mean = np.mean(samples)
            std = np.std(samples)
            return (mean, std)
        else:
            return "lower_bound has to be smaller than upper_bound"
    else:
        return "The inputs for this function need to be of the type int or float."


if __name__ == "__main__":
    print(gaussian_analysis(5,5,0,10))

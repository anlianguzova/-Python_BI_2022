
def gc_content(read, threshold):
    read = read.upper()
    gc_number = 0
    gc_number += read.count('G')
    gc_number += read.count('C')
    gc_percentage = (gc_number / len(read)) * 100

    if type(threshold) is int:
        high_border = threshold
        return gc_percentage < high_border

    if type(threshold) is tuple:
        low_border = threshold[0]
        high_border = threshold[1]
        return low_border < gc_percentage < high_border


def length(read, threshold):
    if type(threshold) is int:
        high_bound = threshold
        return len(read) < high_bound

    if type(threshold) is tuple:
        low_bound = threshold[0]
        high_bound = threshold[1]
        return low_bound < len(read) < high_bound


def mean_quality(q_read, threshold):
    quality = 0
    for i in q_read:
        quality += (ord(i) - 33)
    quality_mean = quality / len(q_read)
    return quality_mean > threshold


def read_scan(lines, gc_bounds=None, length_bounds=None, quality_threshold=None):
    read_res = gc_content(lines[1], gc_bounds) and length(lines[1], length_bounds)
    quality_res = mean_quality(lines[3], quality_threshold)
    return read_res and quality_res


def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), 
         length_bounds=(0, 2**32), quality_threshold=0, save_filtered=False):
    passed_reads = open(output_file_prefix + '_passed.fastq', 'w')
    if save_filtered:
        filtered_reads = open(output_file_prefix + '_filtered.fastq', 'w')

    with open(input_fastq, "r") as fastq_file:
        while True:
            single_id_lines = []
            for i in range(4):
                line = fastq_file.readline()
                single_id_lines.append(line)
            if not line:
                break

            result = read_scan(single_id_lines, gc_bounds, length_bounds, quality_threshold)
            lines = ''.join(single_id_lines)

            if result:
                passed_reads.write(lines)

            if not result and save_filtered:
                filtered_reads.write(lines)




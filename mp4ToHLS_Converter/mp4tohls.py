import os

out_360p = "ffmpeg -i test_vid.mp4 -vf scale=w=640:h=360 -hls_segment_filename ./output/360p_%03d.ts ./output/360p.m3u8"
out_480p = "ffmpeg -i test_vid.mp4 -vf scale=w=768:h=480 -hls_segment_filename ./output/480p_%03d.ts ./output/480p.m3u8"
out_720p = "ffmpeg -i test_vid.mp4 -vf scale=w=1280:h=720 -hls_segment_filename ./output/720p_%03d.ts ./output/720p.m3u8"

filename = input("Filename: ")
out_cmd = ""

print("""
        Output Resolution
        1. 640 x 360 (360p)
        2. 768 x 480 (480p)
        3. 1280 x 720 (720p)
        """)
res_option = input("=> ")

while True:
    if res_option == "1":
        out_cmd = out_360p.replace("test_vid.mp4", filename)
        break
    elif res_option == "2":
        out_cmd = out_480p.replace("test_vid.mp4", filename)
        break
    elif res_option == "3":
        out_cmd = out_720p.replace("test_vid.mp4", filename)
        break
    print("Invalid input. Please select 1, 2, or 3")

while True:
    output_folder_name = input("Output Folder Name: ")
    output_path = os.path.dirname(os.path.realpath(__file__)) + "/" + output_folder_name
    print(output_path)

    if os.path.exists(output_path):
        rewrite = input("File Already Exists, rewrite?(y/n): ")
        if rewrite == "n":
            continue
        else:
            break
    os.mkdir(output_path)
    out_cmd = out_cmd.replace("./output", output_path)
    break

print("Start!!!", out_cmd)
os.system(out_cmd)
print("Done!!!")

from pipeline.outreach_pipeline import OutreachPipeline


def main():

    domain = input(
        "Enter Company Domain: "
    )

    pipeline = OutreachPipeline()

    pipeline.run(domain)


if __name__ == "__main__":
    main()
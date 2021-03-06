# Generated by Django 2.2.7 on 2020-01-23 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '__first__'),
        ('Product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionDetails',
            fields=[
                ('auctiondetails_id', models.AutoField(primary_key=True, serialize=False)),
                ('auctiondetails_baseprice', models.FloatField()),
                ('auctiondetails_date', models.DateTimeField()),
                ('productinformation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.ProductInformation')),
            ],
        ),
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('bidder_id', models.AutoField(primary_key=True, serialize=False)),
                ('bidder_type', models.CharField(max_length=36)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentAuction',
            fields=[
                ('currentauction_id', models.AutoField(primary_key=True, serialize=False)),
                ('auctiondetails', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='Auction.AuctionDetails')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentBid',
            fields=[
                ('currentbid_id', models.AutoField(primary_key=True, serialize=False)),
                ('currentbid_time', models.TimeField()),
                ('currentbid_amount', models.FloatField()),
                ('currentbid_bidderprice', models.FloatField()),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction.Bidder')),
                ('currentauction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction.CurrentAuction')),
            ],
        ),
        migrations.CreateModel(
            name='AutoBid',
            fields=[
                ('autobid_id', models.AutoField(primary_key=True, serialize=False)),
                ('starting_price', models.FloatField()),
                ('increment_price_by', models.FloatField()),
                ('ending_price', models.FloatField()),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction.Bidder')),
            ],
        ),
    ]
